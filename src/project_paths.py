"""Repository-relative inputs and a separate, ignored area for new run outputs."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PROBLEMS_FILE = DATA_DIR / "problems.csv"
RUN_RESULTS_DIR = ROOT / "run-results"
