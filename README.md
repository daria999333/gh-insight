# gh-insight 🚀
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-CLI-green?style=flat-square)
![Pytest](https://img.shields.io/badge/Tests-Passing-brightgreen?style=flat-square&logo=pytest&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

A lightweight CLI tool built with Python to analyze and visualize GitHub user profiles, top repositories, and language statistics directly in your terminal.

## Features

- 👤 Profile Overview: Fetch user bio, follower count, and public repository metrics.
- 📊 Language Breakdown: Calculate language usage percentages across public repositories.
- 🌟 Top Repositories: Display top-rated repositories sorted by stars.
- 🎨 Rich Terminal UI: Beautifully formatted tables and panels powered by rich.

## Tech Stack

- Python 3.10+
- [HTTPX](https://www.python-httpx.org/) — HTTP client for GitHub REST API calls.
- [Rich](https://rich.readthedocs.io/) — Terminal formatting and visuals.
- [Typer](https://typer.tiangolo.com/) — CLI framework.
- [pytest](https://docs.pytest.org/) — Unit testing suite.

## Installation

1. Clone the repository:
  
   git clone [https://github.com/daria999333/gh-insight.git](https://github.com/daria999333/gh-insight.git)
   cd gh-insight
   
2. Create and activate a virtual environment:
  
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   
3. Install dependencies:
  
   pip install -r requirements.txt
   
## Usage

python main.py <github_username>
