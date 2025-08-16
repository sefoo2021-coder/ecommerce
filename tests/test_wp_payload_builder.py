from app.pipeline import publish_wp


def test_wp_payload_builder(monkeypatch):
    monkeypatch.setenv("DRY_RUN", "true")
    item = {"platform": "x", "title": "Hello", "summary": "Hi", "url": "http://example.com"}
    payload = publish_wp.build_payload(item)
    assert payload["title"].startswith("[x]")
    assert "الرابط الأصلي" in payload["content"]
