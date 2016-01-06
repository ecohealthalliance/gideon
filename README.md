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

## License
Copyright 2016 EcoHealth Alliance

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
