# Data

Keep only small metadata or instructions under version control. Large datasets should be downloaded from their original sources or by reproducible scripts and should normally remain untracked.

Suggested layout when needed:

- `data/raw/` — source data, unmodified.
- `data/processed/` — transformed data created by study code.
- `data/downloads/` — archives or temporary downloads.
