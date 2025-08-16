from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List


@dataclass
class RawItem:
    """Represents a fetched entry before normalization."""

    source_name: str
    platform: str
    author: str | None
    title: str
    summary: str | None
    url: str
    published_at: str | None
    raw: Dict[str, Any]


class BaseSource(ABC):
    """Abstract base class for all connectors."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    def fetch(self) -> Iterable[RawItem]:
        """Fetch items from the source."""
        raise NotImplementedError
