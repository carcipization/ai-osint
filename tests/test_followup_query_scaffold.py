from scripts.followup_query_scaffold import build_queries


def test_build_queries_shape_and_content():
    q = build_queries("Red Sea shipping", "insurers", "2026-05", "insurance rates")
    assert set(q.keys()) == {"bluesky", "polymarket", "crosscheck"}
    assert len(q["bluesky"]) >= 3
    assert len(q["polymarket"]) >= 3
    assert "site:bsky.app" in q["bluesky"][0]
    assert "Polymarket" in q["polymarket"][0]
    assert "official update" in q["crosscheck"][0]
