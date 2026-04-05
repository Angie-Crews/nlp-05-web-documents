"""
src/nlp/stage02_validate_crews_p4.py - Validate Stage (Crews Phase 4)

Validates that the expected page structure is present for your crews phase 4 pipeline.
"""

import logging

from bs4 import BeautifulSoup


def run_validate(
    html_content: str,
    LOG: logging.Logger,
) -> BeautifulSoup:
    LOG.info("========================")
    LOG.info("STAGE 02: VALIDATE starting (crews_p4)...")
    LOG.info("========================")
    LOG.info("HTML STRUCTURE INSPECTION:")
    soup = BeautifulSoup(html_content, "html.parser")
    LOG.info(f"Top-level type: {type(soup).__name__}")
    LOG.info(
        f"Top-level elements: {[element.name for element in soup.find_all(recursive=False)]}"
    )
    title = soup.find("h1", class_="title")
    authors = soup.find("div", class_="authors")
    abstract = soup.find("blockquote", class_="abstract")
    subjects = soup.find("div", class_="subheader")
    dateline = soup.find("div", class_="dateline")
    LOG.info("VALIDATE: Title found: %s", title is not None)
    LOG.info("VALIDATE: Authors found: %s", authors is not None)
    LOG.info("VALIDATE: Abstract found: %s", abstract is not None)
    LOG.info("VALIDATE: Subjects found: %s", subjects is not None)
    LOG.info("VALIDATE: Dateline found: %s", dateline is not None)
    missing = []
    if not title:
        missing.append("title")
    if not authors:
        missing.append("authors")
    if not abstract:
        missing.append("abstract")
    if not subjects:
        missing.append("subjects")
    if not dateline:
        missing.append("dateline")
    if missing:
        raise ValueError(
            f"VALIDATE: Required elements missing: {missing}. Page structure may have changed."
        )
    LOG.info("VALIDATE: HTML structure is valid.")
    LOG.info("Sink: validated BeautifulSoup object")
    return soup
