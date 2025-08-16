from __future__ import annotations

import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("WORDPRESS_BASE_URL")
USER = os.getenv("WORDPRESS_USERNAME")
PASSWORD = os.getenv("WORDPRESS_APP_PASSWORD")
DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"


def build_payload(item: Dict[str, str]) -> Dict[str, str]:
    title = f"[{item['platform']}] {item['title']}"
    body = (
        f"{item.get('summary','')}\n"
        f"الرابط الأصلي: {item['url']}\n\n"
        "تحقق الذكاء الاصطناعي:\n"
        f"الحكم: {item.get('llm_verdict','')}\n"
        f"ملاحظات: {item.get('llm_notes','')}\n"
    )
    return {
        "title": title,
        "content": body,
        "status": "draft" if DRY_RUN else "publish",
    }


def publish(item: Dict[str, str]) -> Dict[str, str] | None:
    if DRY_RUN:
        return None
    payload = build_payload(item)
    resp = requests.post(
        f"{BASE_URL}/wp-json/wp/v2/posts",
        auth=(USER, PASSWORD),
        json=payload,
        timeout=20,
    )
    resp.raise_for_status()
    data = resp.json()
    return {"wp_post_id": data["id"], "wp_url": data["link"]}
