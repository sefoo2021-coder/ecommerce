from __future__ import annotations

import os
import datetime as dt
import re
from pathlib import Path
from typing import Dict


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9-]+", "-", text.lower())
    return re.sub(r"-+", "-", text).strip("-")


def export_markdown(item: Dict[str, str]) -> Path:
    date = dt.datetime.utcnow().date().isoformat()
    folder = Path("out") / date
    folder.mkdir(parents=True, exist_ok=True)
    slug = slugify(item["title"])[:60]
    path = folder / f"{slug}.md"
    content = (
        f"# {item['title']}\n\n"
        f"{item.get('summary','')}\n\n"
        f"الرابط: {item['url']}\n"
    )
    path.write_text(content, encoding="utf-8")
    return path
