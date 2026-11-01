# LLM_Development

LLM development experiments and projects.

## Setup

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

On Windows, activate the environment with `.venv\Scripts\activate`.

## Tests

```bash
pytest
```

Check style with Ruff:

```bash
ruff check .
```

## Project layout

```
.
├── notebooks/               # exploratory notebooks
├── scripts/                 # one-off scripts
├── src/llm_development/     # installable package
├── tests/                   # pytest suite
├── pyproject.toml
└── README.md
```
