from __future__ import annotations

from typing import Iterable, List

import snscrape.modules.twitter as sntwitter

from .base import RawItem


def fetch_user(username: str, limit: int = 5) -> Iterable[RawItem]:
    scraper = sntwitter.TwitterUserScraper(username)
    for i, tweet in enumerate(scraper.get_items()):
        if i >= limit:
            break
        yield RawItem(
            source_name=username,
            platform="x",
            author=username,
            title=tweet.content[:80],
            summary=tweet.content,
            url=f"https://x.com/{username}/status/{tweet.id}",
            published_at=tweet.date.isoformat(),
            raw=tweet.__dict__,
        )


def fetch_people(usernames: List[str], limit: int = 5) -> List[RawItem]:
    items: List[RawItem] = []
    for user in usernames:
        items.extend(list(fetch_user(user, limit)))
    return items
