from __future__ import annotations

from typing import Iterable

import feedparser

from .base import BaseSource, RawItem


class YouTubeRSS(BaseSource):
    """Fetch YouTube channel videos via RSS."""

    def fetch(self) -> Iterable[RawItem]:
        parsed = feedparser.parse(self.config["url"])
        for entry in parsed.entries:
            yield RawItem(
                source_name=self.config["name"],
                platform="youtube",
                author=getattr(entry, "author", None),
                title=getattr(entry, "title", ""),
                summary=getattr(entry, "summary", None),
                url=getattr(entry, "link", ""),
                published_at=getattr(entry, "published", None),
                raw=entry,
            )
