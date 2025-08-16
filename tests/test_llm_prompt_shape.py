from app.pipeline import llm_check


def test_llm_prompt_shape():
    item = {"title": "Test", "summary": "Summary", "source_name": "Src", "published_at": "2024"}
    prompt = llm_check.build_prompt(item)
    assert "العنوان" in prompt and "الملخص" in prompt
