# Household Production Analysis

ATUS (American Time Use Survey) analysis of time spent on household production
by married men and women, with and without children.

## Running

```sh
uv sync                         # install dependencies
uv run jupyter lab              # open notebooks
```

The extraction notebook (`01_extraction.ipynb`) downloads ATUS 2018 data
automatically from a GitHub mirror (BLS blocks automated downloads).
