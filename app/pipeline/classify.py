from __future__ import annotations

from typing import Iterable, List

import yaml


def load_topics(path: str) -> List[str]:
    data = yaml.safe_load(open(path, "r", encoding="utf-8"))
    return data.get("topics", [])


def classify(text: str, topics: Iterable[str]) -> List[str]:
    text_lower = text.lower()
    return [t for t in topics if t.lower() in text_lower]
