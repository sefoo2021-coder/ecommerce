from __future__ import annotations

import json
import os
from typing import Dict

from dotenv import load_dotenv
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def build_prompt(item: Dict[str, str]) -> str:
    return (
        f"العنوان: {item['title']}\n"
        f"الملخص: {item.get('summary','')}\n"
        f"المصدر: {item['source_name']}\n"
        f"التاريخ: {item.get('published_at','')}"
    )


@retry(wait=wait_exponential(multiplier=1, min=1, max=4), stop=stop_after_attempt(3))
def check_item(item: Dict[str, str]) -> Dict[str, str]:
    prompt = build_prompt(item) + "\nأجب بصيغة JSON كما هو محدد."
    response = client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "system",
                "content": "أنت مساعد تتحقق من الأخبار التسويقية.",
            },
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        timeout=15,
    )
    data = json.loads(response.output[0].content[0].text)
    return {
        "llm_verdict": data.get("verdict"),
        "llm_notes": data.get("notes"),
        "llm_sources_json": json.dumps(data.get("sources", [])),
    }
