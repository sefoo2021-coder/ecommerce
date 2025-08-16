from __future__ import annotations

import datetime as dt
from typing import Iterable

import feedparser

from .base import BaseSource, RawItem


class RSSSource(BaseSource):
    """Generic RSS/Atom reader."""

    def fetch(self) -> Iterable[RawItem]:
        parsed = feedparser.parse(self.config["url"])
        for entry in parsed.entries:
            published = None
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                published = dt.datetime(*entry.published_parsed[:6]).isoformat()
            yield RawItem(
                source_name=self.config["name"],
                platform=self.config.get("platform", "rss"),
                author=getattr(entry, "author", None),
                title=getattr(entry, "title", ""),
                summary=getattr(entry, "summary", None),
                url=getattr(entry, "link", ""),
                published_at=published,
                raw=entry,
            )
