from app.pipeline import classify


def test_classify_topics(tmp_path):
    topics = ["Meta Ads", "TikTok Shop"]
    text = "New features in TikTok Shop for sellers"
    result = classify.classify(text, topics)
    assert result == ["TikTok Shop"]
