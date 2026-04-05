"""
src/nlp/config_crews_p4.py - Crews Phase 4 Configuration

Stores configuration values for the web document EVTL pipeline (crews phase 4 version).
"""

from pathlib import Path

PAGE_URL: str = "https://arxiv.org/abs/2602.20021"  # Update for Phase 5
HTTP_REQUEST_HEADERS: dict = {
    "User-Agent": "Mozilla/5.0 (educational-use; web-mining-course)"
}

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

RAW_HTML_PATH: Path = RAW_PATH / "crews_p4_raw.html"  # Phase 4 output
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "crews_p4_processed.csv"
