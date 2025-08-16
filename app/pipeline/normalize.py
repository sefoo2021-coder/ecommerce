from __future__ import annotations

import hashlib
from typing import Any, Dict

from bs4 import BeautifulSoup
from markdownify import markdownify as md

from app.sources.base import RawItem


def clean_html(html: str | None) -> str | None:
    if not html:
        return None
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(" ", strip=True)


def normalize(item: RawItem) -> Dict[str, Any]:
    """Return normalized dict for DB insertion."""
    summary = clean_html(item.summary)
    return {
        "hash": hashlib.sha256(f"{item.source_name}|{item.url}|{item.title}".encode()).hexdigest(),
        "source_name": item.source_name,
        "platform": item.platform,
        "author": item.author,
        "title": item.title,
        "summary": summary,
        "url": item.url,
        "published_at": item.published_at,
    }
