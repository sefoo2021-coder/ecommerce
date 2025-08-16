from __future__ import annotations

import datetime as dt
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy import JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    kind = Column(String)
    url = Column(String)
    platform = Column(String)
    last_checked_at = Column(DateTime)
    enabled = Column(Boolean, default=True)


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform = Column(String)
    urls_json = Column(Text)
    enabled = Column(Boolean, default=True)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    hash = Column(String, unique=True)
    source_id = Column(Integer)
    author = Column(String)
    title = Column(String)
    summary = Column(Text)
    url = Column(String)
    platform = Column(String)
    published_at = Column(String)
    is_from_tracked_person = Column(Boolean, default=False)
    topics_json = Column(Text)
    llm_verdict = Column(String)
    llm_notes = Column(Text)
    llm_sources_json = Column(Text)
    created_at = Column(DateTime, default=dt.datetime.utcnow)
    posted_to_wp = Column(Boolean, default=False)


class Run(Base):
    __tablename__ = "runs"
    id = Column(Integer, primary_key=True)
    started_at = Column(DateTime, default=dt.datetime.utcnow)
    finished_at = Column(DateTime)
    status = Column(String)
    stats_json = Column(Text)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer)
    wp_post_id = Column(Integer)
    wp_url = Column(String)
    published_at = Column(DateTime)
