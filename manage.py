from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.pipeline import classify, dedupe, export_md, llm_check, normalize, publish_wp
from app.sources import rss
from app.db import models

load_dotenv()
DB_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
engine = create_engine(DB_URL)
models.Base.metadata.create_all(engine)


def load_feeds() -> list[dict]:
    return yaml.safe_load(open("app/config/feeds.yaml", "r", encoding="utf-8"))


def ingest(session: Session, limit: int) -> list[dict]:
    items = []
    topics = classify.load_topics("app/config/topics.yaml")
    for feed in load_feeds():
        if not feed.get("enabled"):
            continue
        source = rss.RSSSource(feed)
        for raw in source.fetch():
            norm = normalize.normalize(raw)
            if dedupe.is_duplicate(session, norm["hash"]):
                continue
            norm["topics_json"] = json.dumps(
                classify.classify(f"{norm['title']} {norm.get('summary','')}", topics)
            )
            items.append(norm)
            if len(items) >= limit:
                return items
    return items


def process_and_publish(session: Session, items: list[dict]) -> None:
    for item in items:
        item.update(llm_check.check_item(item))
        publish_wp.publish(item)
        export_md.export_markdown(item)
        db_item = models.Item(**item)
        session.add(db_item)
    session.commit()


def run_once(limit: int) -> None:
    with Session(engine) as session:
        items = ingest(session, limit)
        process_and_publish(session, items)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("run-once", nargs="?", help="run pipeline once")
    parser.add_argument("--limit", type=int, default=int(os.getenv("MAX_ITEMS_PER_RUN", "50")))
    args = parser.parse_args()
    run_once(args.limit)
