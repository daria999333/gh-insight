from typing import Any
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def render_profile_card(profile: dict[str, Any]) -> None:
    """Renders a card with primary profile information."""
    name = profile.get("name") or profile.get("login", "Unknown")
    login = profile.get("login", "")
    bio = profile.get("bio") or "No bio provided"
    followers = profile.get("followers", 0)
    following = profile.get("following", 0)
    public_repos = profile.get("public_repos", 0)
    location = profile.get("location") or "Not specified"

    content = (
        f"[bold cyan]Name:[/bold cyan] {name} (@{login})\n"
        f"[bold cyan]Bio:[/bold cyan] {bio}\n"
        f"[bold cyan]Location:[/bold cyan] {location}\n\n"
        f"Followers: [bold green]{followers}[/bold green]  |  "
        f"Following: [bold green]{following}[/bold green]  |  "
        f"Repositories: [bold yellow]{public_repos}[/bold yellow]"
    )

    panel = Panel(
        content,
        title="[bold magenta]GitHub Profile[/bold magenta]",
        border_style="magenta",
        expand=False,
    )
    console.print(panel)


def render_top_repos(repos: list[dict[str, Any]], limit: int = 5) -> None:
    """Displays a table of top-rated repositories."""
    sorted_repos = sorted(
        repos, key=lambda r: r.get("stargazers_count", 0), reverse=True
    )[:limit]

    table = Table(
        title=f"Top-{len(sorted_repos)} Repositories",
        show_header=True,
        header_style="bold blue",
    )
    table.add_column("Repository", style="bold white")
    table.add_column("Language", style="cyan")
    table.add_column("Stars", justify="right", style="yellow")
    table.add_column("Forks", justify="right", style="green")

    for repo in sorted_repos:
        table.add_row(
            repo.get("name", "N/A"),
            repo.get("language") or "N/A",
            str(repo.get("stargazers_count", 0)),
            str(repo.get("forks_count", 0)),
        )

    console.print(table)


def render_language_stats(stats: dict[str, float]) -> None:
    """Displays a table showing programming language statistics."""
    if not stats:
        console.print("[yellow]No programming language data available.[/yellow]")
        return

    table = Table(
        title="Language Breakdown",
        show_header=True,
        header_style="bold green",
    )
    table.add_column("Language", style="bold white")
    table.add_column("Share", justify="right", style="magenta")

    for lang, percentage in stats.items():
        table.add_row(lang, f"{percentage}%")

    console.print(table)