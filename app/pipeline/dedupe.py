from __future__ import annotations

from sqlalchemy.orm import Session

from app.db import models


def is_duplicate(session: Session, item_hash: str) -> bool:
    return session.query(models.Item).filter_by(hash=item_hash).first() is not None
