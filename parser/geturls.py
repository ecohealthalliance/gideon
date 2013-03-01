import sys
import os # Use os.chdir to open file
import csv
import bs4
import lxml
import re
# import pdb

# pdb.set_trace()

# We will be using this often.
Tag = bs4.element.Tag

# Create csv readers

# Compile regex patterns
pre = re.compile('[0-9]{5}')
lre = re.compile('G[0-9]{3}')

datadir = "../data/"
indir = "raw/"
outdir = "processed/"
infile = "gideon-outbreaks-only.html"
outfile = "gideon-outbreak-urls.csv"

os.chdir(datadir)
outbreakhtml = open(indir + infile, 'r')

outbreaksoup = bs4.BeautifulSoup(outbreakhtml, "lxml")
outbreaktags = outbreaksoup.html.body.children



# Dont think we need this:
# def b_parse(outbreak_b):
#     """Should set disease name to string of tag"""
#     outbreak_pathogen = item.string

def ul_scrape(outbreak_ul):
    """Iterates through <ul>s pulling out year, location and url."""
    years = []
    locations = []
    urls = []
    pids = []
    lids = []
    for desc in outbreak_ul.descendants:
        if isinstance(desc, Tag) and desc.name is "b":
            years.append(desc.contents)
        elif isinstance(desc, Tag) and desc.name is "a":
            locations.append(desc.contents)
            url = desc['href']
            urls.append(url)
            pids.append(pre.match(url).group())
            lids.append(lre.match(url).group())
    return zip(years, locations, urls, pids, lids)

def writeout(pathogen, outbreaks):
    """Writes all data for a particular pathogen"""
    for year, location, url, pid, lid in outbreaks:
        print pathogen, year, location, url, pid, lid


# Use it:

# def main():
"""Loops through items in soup, passing to functions as
appropriate"""
for item in outbreaktags:
    if isinstance(item, Tag) and item.name is 'b':
        pathogen = item.string
    elif isinstance(item, Tag) and item.name is 'ul':
        outbreakzip = ul_scrape(item)
        writeout(pathogen, outbreakzip)

# if __name__ == '__main__':
#     main()

"""Main loop pseudocode:

find pathogens in soup
    for pathogen in soup
        pathogen = pathogen
        find years in pathogen
        for year in pathogen
            year = year
            find outbreaks in year
            for outbreaks in year
                country = country
                url = url
                countrycode = countrycode
                pathogencode = pathogencode
                write csv line with pathogen, year, country, url,
                                    countrycode, pathogencode

"""