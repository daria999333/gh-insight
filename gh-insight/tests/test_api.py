from unittest.mock import patch
from gh_insight.api import calculate_language_stats, get_user_profile


def test_calculate_language_stats():
    """Test language percentage calculations with valid data."""
    repos = [
        {"language": "Python"},
        {"language": "Python"},
        {"language": "JavaScript"},
        {"language": None}, 
    ]
    stats = calculate_language_stats(repos)
    assert stats == {"Python": 66.7, "JavaScript": 33.3}


def test_calculate_language_stats_empty():
    """Test language statistics with empty repository list."""
    assert calculate_language_stats([]) == {}


@patch("gh_insight.api.httpx.get")
def test_get_user_profile_not_found(mock_get):
    """Test handling of 404 Not Found response from GitHub API."""
    class MockResponse:
        status_code = 404

    mock_get.return_value = MockResponse()
    result = get_user_profile("nonexistent_user_abc123")
    assert result is None