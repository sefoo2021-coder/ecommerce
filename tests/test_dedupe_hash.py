from app.sources.base import RawItem
from app.pipeline import normalize


def test_dedupe_hash():
    item1 = RawItem("Source", "platform", "author", "Title", "Summary", "http://a", "2024-01-01", {})
    item2 = RawItem("Source", "platform", "author", "Title", "Summary", "http://a", "2024-01-01", {})
    norm1 = normalize.normalize(item1)
    norm2 = normalize.normalize(item2)
    assert norm1["hash"] == norm2["hash"]
