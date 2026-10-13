import typer
from rich.console import Console

from gh_insight.api import (
    calculate_language_stats,
    get_user_profile,
    get_user_repos,
)
from gh_insight.formatter import (
    render_language_stats,
    render_profile_card,
    render_top_repos,
)

app = typer.Typer(help="GitHub profile and repository statistics analyzer CLI.")
console = Console()


@app.command()
def analyze(username: str = typer.Argument(..., help="GitHub username to analyze")) -> None:
    """Analyze GitHub profile, repositories, and primary programming languages."""
    console.print(f"\n[bold yellow]Fetching data for @{username}...[/bold yellow]\n")

    profile = get_user_profile(username)
    if not profile:
        console.print(f"[bold red]Error:[/bold red] User '{username}' not found.")
        raise typer.Exit(code=1)

    repos = get_user_repos(username) or []

    
    render_profile_card(profile)
    console.print()

    if repos:
        render_top_repos(repos)
        console.print()
        lang_stats = calculate_language_stats(repos)
        render_language_stats(lang_stats)
    else:
        console.print("[yellow]No public repositories found for this user.[/yellow]")

    console.print("\n[bold green]Analysis complete![/bold green]\n")


if __name__ == "__main__":
    app()