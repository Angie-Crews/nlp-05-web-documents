"""
src/nlp/pipeline_web_html_crews_p5.py - Crews Phase 5 Pipeline Script

Orchestrates the EVTL pipeline using your crews phase 5 config, validate, and transform modules.
"""

import logging

from datafun_toolkit.logger import get_logger, log_header, log_path

from nlp.config_crews_p5 import (
    DATA_PATH,
    HTTP_REQUEST_HEADERS,
    PAGE_URL,
    PROCESSED_CSV_PATH,
    PROCESSED_PATH,
    RAW_HTML_PATH,
    RAW_PATH,
    ROOT_PATH,
)
from nlp.stage01_extract import run_extract
from nlp.stage02_validate_crews_p5 import run_validate
from nlp.stage03_transform_crews_p5 import run_transform
from nlp.stage04_load import run_load

LOG: logging.Logger = get_logger("CI", level="DEBUG")


def main() -> None:
    log_header(LOG, "Module 5: EVTL PIPELINE - WEB DOCUMENTS (CREWS_P5)")
    LOG.info("START PIPELINE (crews_p5)")
    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DATA_PATH", DATA_PATH)
    log_path(LOG, "RAW_PATH", RAW_PATH)
    log_path(LOG, "PROCESSED_PATH", PROCESSED_PATH)

    html_content = run_extract(
        source_url=PAGE_URL,
        http_request_headers=HTTP_REQUEST_HEADERS,
        raw_html_path=RAW_HTML_PATH,
        LOG=LOG,
    )
    validated_soup = run_validate(
        html_content=html_content,
        LOG=LOG,
    )
    df = run_transform(
        soup=validated_soup,
        LOG=LOG,
    )
    run_load(
        df=df,
        processed_csv_path=PROCESSED_CSV_PATH,
        LOG=LOG,
    )

    LOG.info("========================")
    LOG.info("Pipeline executed successfully! (crews_p5)")
    LOG.info("========================")


if __name__ == "__main__":
    main()
