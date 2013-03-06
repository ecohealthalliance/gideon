gideon
======

Tools for interacting with GIDEON.

gidcommon.py
------------

Imports `sys`, `os`, and `csv`.

Sets variables:

- `datadir = "../data/"`
- `indir = "raw/"`
- `outdir = "processed/"`

geturls.py
----------

`geturls.py` extracts a csv table of outbreaks from the html of GIDEON's outbreak list.

- Looks for `gideon-outbreaks-only.html` in the `data/raw/` directory.
- Crawls through the list, gathering for each outbreak pathogen, year, location, url, and the pathogen and location ID.
- Outputs these to `gideon-outbreaks-csv.csv` in `data/processed`.

first-try
---------

- **gideon_dump.txt** is a copied/pasted list of outbreaks from the site
- **gideon_parser.py** reformats that list into a nice csv file
- **gdatabase.csv** is the nice csv file, listing outbreaks by disease / year / country
