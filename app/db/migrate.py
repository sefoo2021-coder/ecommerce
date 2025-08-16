from __future__ import annotations

import os

from sqlalchemy import create_engine

from . import models

DB_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

def migrate() -> None:
    engine = create_engine(DB_URL)
    models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    migrate()
