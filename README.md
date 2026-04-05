# nlp-05-web-documents

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Structured EVTL pipeline for reliable extraction and transformation of data from HTML web pages.

Web Mining and Applied NLP require reliable acquisition and
processing of structured and semi-structured text data.
This project implements a reproducible pipeline for
working with HTML data from web pages.

The pipeline follows an EVTL architecture:

- Extract HTML from a web page
- Validate structure and content before use
- Transform HTML into a structured representation
- Load results into a persistent, analyzable format

The emphasis is on correctness, inspectability, and repeatability:
every stage has explicit inputs, outputs, and logging,
and intermediate artifacts are preserved for verification.

## This Project

This project demonstrates how to work with
HTML data retrieved from web pages using a structured EVTL pipeline.

The workflow:

- Acquire HTML from an external web page
- Inspect and validate its structure
- Transform it into a tabular representation
- Persist results for downstream analysis

Each stage is implemented as a modular component with explicit inputs and outputs.

## Key Files

These files define the EVTL pipeline and the components you will update for your project.

- **src/nlp/pipeline_web_html.py** - Main pipeline orchestrator (no changes required)
- **src/nlp/config_case.py** - Configuration for page URL and paths (<mark>**copy and edit**</mark> for your project)
- **src/nlp/stage01_extract.py** - Extract stage: fetches HTML from a web page (no changes required)
- **src/nlp/stage02_validate_case.py** - Validate stage: inspects and verifies HTML structure (<mark>**copy and edit**</mark>)
- **src/nlp/stage03_transform_case.py** - Transform stage: converts HTML into structured data (<mark>**copy and edit**</mark>)
- **src/nlp/stage04_load.py** - Load stage: writes output to persistent storage (no changes required)
- **pyproject.toml** - Project metadata and dependencies (<mark>**update**</mark> authorship, links, and dependencies)
- **zensical.toml** - Documentation configuration (<mark>**update**</mark> authorship and links)

## CC5.2: Set Up & Verify Project – Due April 8, 2026

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

## Phase 1. **Start & Run**

### Start in GitHub to Copy a Template Repository

1. Log in to GitHub and open the example project repository in your browser.
2. Click **Use this template** and choose **Create a new repository**.
3. Confirm that the **Owner** is your GitHub account.
4. Keep the repository name so it continues to reflect the associated skills, and do not use spaces.
5. Set the repository visibility to **Public** so others can view your work.
6. If preferred, use a fake name or alias on GitHub.
7. Click **Create repository** to finish creating your copy.

### Configure Repository Settings

Enable GitHub Pages so your repository can publish a professional documentation site for project instructions, setup steps, and technical notes.

1. In your new repository, click the **Settings** tab.
2. In the left sidebar, select **Pages**.
3. Under **Build and deployment** and **Source**, choose **GitHub Actions**.
4. Click the **Code** tab to return to the main repository view.


### Clone a Repository to your Machine

Clone your GitHub repository to your local machine so you can work with the project in VS Code and from a terminal.

1. In your browser, open the repository in your own GitHub account and copy its full URL from the address bar.
2. Open a terminal in your main repositories folder, such as `C:\Repos` on Windows or `~/Repos` on macOS/Linux.
3. Use `git clone` followed by the repository URL you copied, then run the command.
4. Make sure you are using your own GitHub account name and exact repository name in the URL.
5. Verify that a new local folder with the repository name appears and that the terminal shows no authentication or repository-not-found errors.

Example commands:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/Angie-Crews/nlp-05-web-documents
cd nlp-05-web-documents
code .
```

### Open the Project in VS Code (and Install Recommended VS Code Extensions)

Open the cloned repository as a VS Code workspace so you can use the project files, terminal, and recommended development extensions.

1. In a terminal opened in your main repositories folder, change into your repository directory and run `code .`.
2. Make sure you use your exact repository name when running `cd`.
3. When VS Code opens, install any recommended extensions that appear in the popup.
4. If the project includes `.vscode/extensions.json`, VS Code will usually recommend the extensions listed there.
5. If no recommendations appear, open the Extensions view with **View > Extensions** or `Ctrl+Shift+X` on Windows/Linux and search for the extensions manually.
6. Do not install `ms-python.black-formatter` or `ms-python.autopep8` for this workflow because Ruff handles formatting and linting.
7. Additional extensions can be added later if your work requires them.

### Set up Project Python Environment (managed by uv)

Use a VS Code terminal to create and sync the project environment with `uv`, then reload VS Code so the Python language tools pick up the environment correctly.

1. Run the setup commands below in a VS Code terminal.
2. After the environment is created, open the Command Palette.
3. Run **Developer: Reload Window** to restart the Python language server and refresh the workspace.

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files

# Later, we install spacy data model and
# en_core_web_sm = english, core, web, small
# It's big: spacy+data ~200+ MB w/ model installed
#           ~350–450 MB for .venv is normal for NLP
# uv run python -m spacy download en_core_web_sm
```

### Run the Code

```shell
# IMPORTANT: Close each figure after viewing so execution continues
uv run python -m nlp.pipeline_web_html
```

### As Needed -- Add / Update Dependencies

```shell
uv cache clean
uv sync --extra dev --extra docs --upgrade
```

### Run checks and Tests (as available)

```shell
uv run ruff format .
uv run ruff check . --fix
uv run zensical build
```

### Build Documentation

```shell
uv run zensical build
uv run zensical serve
```

### Git Add-Commit-Push to GitHub

```shell
git add -A
git commit -m "update"

git add -A
git commit -m "update"

git push -u origin main
```

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Example Artifact (Output)

```text
START PIPELINE
ROOT_PATH = .
DATA_PATH = data
RAW_PATH = data\raw
PROCESSED_PATH = data\processed
========================
STAGE 01: EXTRACT starting...
========================
SOURCE URL = https://arxiv.org/abs/2602.20021
SINK PATH = data\raw\case_raw.html
========================
STAGE 02: VALIDATE starting...
========================
HTML STRUCTURE INSPECTION:
Top-level type: BeautifulSoup
Top-level elements: ['html']
VALIDATE: Title found: True
VALIDATE: Authors found: True
VALIDATE: Abstract found: True
VALIDATE: Subjects found: True
VALIDATE: Dateline found: True
VALIDATE: HTML structure is valid.
Sink: validated BeautifulSoup object
========================
STAGE 03: TRANSFORM starting...
========================
Transformation complete.
DataFrame preview:
   arxiv_id            title  ... abstract_word_count  author_count
0  2602.20021  Agents of Chaos  ...                177            38
Sink: Pandas DataFrame created
========================
STAGE 04: LOAD starting...
========================
SINK PATH = data\processed\case_processed.csv
========================
Pipeline executed successfully!
========================
```

## Enhancements

In production systems, validation is often automated using tools
such as **Great Expectations** or **Soda**.

Within the EVTL architecture, **VALIDATE** is a key stage
with a clear source, process, and sink:

- **Source**: HTML fetched from the web page
- **Process**: parsing with BeautifulSoup, checking structure, confirming expected elements are present
- **Sink**: BeautifulSoup object passed to the TRANSFORM stage

This stage ensures the data is in a **consistent and reliable form**
before transformation begins,
so later steps can run without errors or unexpected results.

In this project, validation is implemented directly,
so all checks are visible, repeatable, and easy to review as part
of the pipeline.

### Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is an important part of implementing professional projects.

### Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
running on your machine, and running the example will print out:

```shell
========================
Pipeline executed successfully!
========================
```

The following artifacts will be created:

- project.log - confirming successful run
- data/raw/case_raw.json - dump of the fetched JSON
- data/processed/case_processed.csv - final loaded result


## Phase 2. **Change Authorship**

### Pull Code from GitHub

```Shell
git pull origin main
```

1. Files updated: `CITATION.cff`, `LICENSE`, `zensical.toml` and GitHub About section
2. Changes made: Updated citation metadata with the current repository URL and author information, added the new author copyright line in the license, and changed the documentation site and repository settings in the Zensical configuration to the current GitHub account and repository.
3. Reason for change: Align project authorship, attribution, and published documentation settings with the new repository owner and project copy.
4. Verification: Checked that the repository links in `CITATION.cff` and `zensical.toml` point to `Angie-Crews/nlp-05-web-documents`, confirmed the added author appears in the citation metadata, and confirmed the license includes the 2026 copyright line for Angie Crews.

## Phase 3. **Read & Understand**

1. Select an interesting part of the example code (`3-10 lines)
  ![Phase 3 Code Chosen](site/assets/images/phase_3_code_chosen.png)
2. Why did you choose this part? It shows how data is pulled from a website, checked for errors, and saved in a way that can be reused in a larger workflow.
3. As an analyst, what could you do with these skills? Automatically collect data, make sure it’s accurate, and build repeatable processes for reports, dashboards, or analysis.


### Key Insights from the Data

The processed data reveals several important findings:

- **Large, Diverse Collaboration:** The case study features 38 authors, indicating a highly collaborative research effort.
- **Focus on AI Agent Vulnerabilities:** The main subject is the security, privacy, and governance risks of autonomous language-model-powered agents in real-world settings.
- **Empirical Evidence of Risks:** The study documents concrete examples of agent failures, including unauthorized compliance, information disclosure, destructive actions, denial-of-service, identity spoofing, and system takeover.
- **Urgency for Policy and Research:** The findings highlight unresolved questions about accountability and responsibility, emphasizing the need for urgent attention from legal, policy, and research communities.

These insights underscore the importance of robust validation and monitoring when deploying autonomous agents, and the value of structured pipelines for extracting actionable knowledge from complex web data.

## Phase 4. **Make a Technical Modification**

1. What specifically did you modify:
  Created a Phase 4 version of the pipeline named `crews_p4` and updated the transform stage to extract two additional fields from the arXiv page: a direct PDF URL and the paper's primary subject code. These values are written to the output as `crews_p4_pdf_url` and `crews_p4_primary_subject_code`.

2. Why did you choose this:
  The PDF URL makes it possible to automate access to the full paper, and the primary subject code makes it easier to classify, filter, and organize research articles by topic.

3. What did you observe:
  When first changes were implemented, both new fields returned `unknown`. After inspecting the raw HTML, it was found that the PDF URL was stored in a `meta` tag named `citation_pdf_url`, and the subject code appeared inside a `span` with class `primary-subject`. After updating the selectors to match the actual page structure, the pipeline ran successfully and both new fields were populated correctly.

4. What insights did you gain:
  Web extraction depends heavily on the actual HTML structure, not assumptions about what the page should look like. Even when a page visually shows the information, the data may be stored in different tags than expected. I also saw the value of using the raw HTML file as evidence when debugging extraction logic.
