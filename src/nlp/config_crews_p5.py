"""
src/nlp/config_crews_p5.py - Crews Phase 5 Configuration

Stores configuration values for the web document EVTL pipeline (crews phase 5 version).
Update PAGE_URL to point to the new problem you want to solve.
"""

from pathlib import Path

PAGE_URL: str = "https://arxiv.org/abs/1706.03762"  # Attention Is All You Need
HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

RAW_HTML_PATH: Path = RAW_PATH / "crews_p5_raw.html"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "crews_p5_processed.csv"
