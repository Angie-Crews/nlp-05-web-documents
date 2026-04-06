"""
src/nlp/stage03_transform_crews_p5.py - Transform Stage (Crews Phase 5)

Transforms validated BeautifulSoup object into a structured DataFrame for your crews phase 5 pipeline.
"""

import logging
import re

from bs4 import BeautifulSoup, Tag
import pandas as pd


def run_transform(
    soup: BeautifulSoup,
    LOG: logging.Logger,
) -> pd.DataFrame:
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting (crews_p5)...")
    LOG.info("========================")

    title_tag: Tag | None = soup.find("h1", class_="title")
    authors_tag: Tag | None = soup.find("div", class_="authors")
    abstract_tag: Tag | None = soup.find("blockquote", class_="abstract")

    title: str = (
        title_tag.get_text(strip=True).replace("Title:", "").strip()
        if title_tag
        else "unknown"
    )
    author_tags_list: list[Tag] = authors_tag.find_all("a") if authors_tag else []
    authors: str = (
        ", ".join(tag.get_text(strip=True) for tag in author_tags_list)
        .replace("Authors:", "")
        .strip()
        if authors_tag
        else "unknown"
    )
    abstract: str = (
        abstract_tag.get_text(strip=True).replace("Abstract:", "").strip()
        if abstract_tag
        else "unknown"
    )

    primary_subject_span: Tag | None = soup.find("span", class_="primary-subject")
    if primary_subject_span:
        subjects = primary_subject_span.get_text(strip=True)
        subject_match = re.search(r"\(([^)]+)\)", subjects)
        primary_subject_code = subject_match.group(1) if subject_match else "unknown"
    else:
        subjects = "unknown"
        primary_subject_code = "unknown"

    dateline: Tag | None = soup.find("div", class_="dateline")
    date_submitted_str: str = dateline.get_text(strip=True) if dateline else "unknown"

    canonical: Tag | None = soup.find("link", rel="canonical")
    if canonical is None:
        LOG.warning("Canonical link not found, setting arXiv ID to 'unknown'")
        arxiv_id: str = "unknown"
    else:
        href: str = str(canonical["href"])
        arxiv_id = href.split("/abs/")[-1]

    pdf_meta_tag: Tag | None = soup.find("meta", attrs={"name": "citation_pdf_url"})
    if pdf_meta_tag and pdf_meta_tag.has_attr("content"):
        pdf_url = pdf_meta_tag["content"]
    else:
        pdf_url = "unknown"

    abstract_word_count: int = len(abstract.split()) if abstract != "unknown" else 0
    author_count: int = (
        len([name.strip() for name in authors.split(",")])
        if authors != "unknown"
        else 0
    )

    record = {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "subjects": subjects,
        "submitted": date_submitted_str,
        "abstract": abstract,
        "abstract_word_count": abstract_word_count,
        "author_count": author_count,
        "crews_p5_pdf_url": pdf_url,
        "crews_p5_primary_subject_code": primary_subject_code,
    }
    df = pd.DataFrame([record])
    LOG.info(f"Created DataFrame with {len(df)} row and {len(df.columns)} columns")
    LOG.info(f"Columns: {list(df.columns)}")
    LOG.info(f"DataFrame preview:\n{df.head()}")
    LOG.info("Sink: Pandas DataFrame created")
    LOG.info("Transformation complete.")
    return df
