from __future__ import annotations

import json
import os

import streamlit as st
import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db import models

DB_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
engine = create_engine(DB_URL)


st.set_page_config(page_title="Ecom Updates Dashboard", layout="wide")


def load_yaml(path: str):
    return yaml.safe_load(open(path, "r", encoding="utf-8"))


with st.sidebar:
    st.title("لوحة التحكم")
    page = st.radio("اختر التبويب", ["Feed", "People", "Sources", "Settings"])


if page == "Feed":
    with Session(engine) as session:
        items = session.query(models.Item).order_by(models.Item.id.desc()).all()
    data = [
        {
            "id": i.id,
            "title": i.title,
            "platform": i.platform,
            "verdict": i.llm_verdict,
        }
        for i in items
    ]
    st.dataframe(data)

elif page == "People":
    people = load_yaml("app/config/people.yaml")
    st.write(people)

elif page == "Sources":
    feeds = load_yaml("app/config/feeds.yaml")
    st.write(feeds)

elif page == "Settings":
    st.write({
        "DRY_RUN": os.getenv("DRY_RUN"),
        "MAX_ITEMS_PER_RUN": os.getenv("MAX_ITEMS_PER_RUN"),
    })
    if st.button("Run Now"):
        from manage import run_once

        run_once(int(os.getenv("MAX_ITEMS_PER_RUN", "50")))
        st.success("Completed run")
