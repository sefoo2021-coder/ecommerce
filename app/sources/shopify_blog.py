from __future__ import annotations

from typing import Iterable

from .rss import RSSSource
from .base import RawItem


class ShopifyBlog(RSSSource):
    """Example connector for Shopify blogs using RSS."""

    def fetch(self) -> Iterable[RawItem]:
        yield from super().fetch()
