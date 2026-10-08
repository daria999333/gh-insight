from typing import Any
import httpx

BASE_URL = "https://api.github.com"


def get_user_profile(username: str) -> dict[str, Any] | None:
    url = f"{BASE_URL}/users/{username}"
    try:
        response = httpx.get(url, timeout=10.0)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError:
        return None


def get_user_repos(username: str) -> list[dict[str, Any]] | None:
    url = f"{BASE_URL}/users/{username}/repos?per_page=100"
    try:
        response = httpx.get(url, timeout=10.0)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError:
        return None


def calculate_language_stats(repos: list[dict[str, Any]]) -> dict[str, float]:
    languages: dict[str, int] = {}
    total_count = 0

    for repo in repos:
        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
            total_count += 1

    if not total_count:
        return {}

    return {
        lang: round((count / total_count) * 100, 1)
        for lang, count in languages.items()
    }