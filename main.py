import sys
from pathlib import Path

# Add src folder to Python module search path
sys.path.append(str(Path(__file__).parent / "src"))

from gh_insight.cli import app

if __name__ == "__main__":
    app()