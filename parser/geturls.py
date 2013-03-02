import sys
import os # Use os.chdir to open file
import csv
import bs4
import lxml
import re
import pdb

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

# Returns true if an item is a bs4 tag.
def isTag(item):
    if isinstance(item, bs4.element.Tag):
        return True
    return False

# We make our soup and strain out everything that isn't a tag.
outbreaksoup = bs4.BeautifulSoup(outbreakhtml, "lxml")
outbreaktags = [child for child in outbreaksoup.html.body.children 
                if isTag(child)]

class Pathogen:
    """Container for outbreak data."""
    def __init__(self, name):
        self.name = name
        self.years = []
        self.locations = []
        self.urls = []
        self.pids = []
        self.lids = []

# Goes through every tag in the soup.
    # If it's a <b> tag, it's a pathogen name.
    # If it's an <ul> tag, it's a list of outbreak years and locations.
def outbreak_crawl():
    for tag in outbreaktags:
        if tag.name is 'b':
            pathogen = Pathogen(tag.string)
        elif tag.name is 'ul':
            handle_ul(tag)
            write_pathogen_data()

# Iterates through <ul> tags that contain year, location and url.
def handle_ul(ul):
    ulcontents = [desc for desc in ul.descendants if isTag(desc)]
    for tag in ulcontents:
        if tag.name is "b":
            pathogen.years.append(tag.contents)
        elif tag.name is "a":
            pathogen.locations.append(tag.contents)
            url = tag['href']
            pathogen.urls.append(url)
            pathogen.pids.append(pre.match(url).group())
            pathogen.lids.append(lre.match(url).group())

# Writes out all the data for a particular pathogen.
def write_pathogen_data():
    pathogenzip = zip(pathogen.years, pathogen.locations, pathogen.urls,
                      pathogen.pids, pathogen.lids)
    for i in pathogenzip:
        print pathogen.name, i

# pdb.set_trace()

if __name__ == '__main__':
    outbreak_crawl()