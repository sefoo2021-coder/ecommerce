from __future__ import annotations

from typing import Iterable

import feedparser

from .base import BaseSource, RawItem


class TelegramRSSHub(BaseSource):
    """Read Telegram channels via RSSHub."""

    def fetch(self) -> Iterable[RawItem]:
        parsed = feedparser.parse(self.config["url"])
        for entry in parsed.entries:
            yield RawItem(
                source_name=self.config["name"],
                platform="telegram",
                author=getattr(entry, "author", None),
                title=getattr(entry, "title", ""),
                summary=getattr(entry, "summary", None),
                url=getattr(entry, "link", ""),
                published_at=getattr(entry, "published", None),
                raw=entry,
            )
