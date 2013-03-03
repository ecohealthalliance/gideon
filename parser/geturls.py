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

outbreaksoup = bs4.BeautifulSoup(outbreakhtml, "lxml")

class OutbreakData:
    """Container for outbreak data."""
    def __init__(self):
        self.pathogens = []
        self.years = []
        self.locations = []
        self.urls = []
        self.pathids = []
        self.locids = []

    # Goes through every tag in the soup.
    # If it's a <b> tag, it's a pathogen name.
    # If it's an <ul> tag, it's a list of outbreak years and locations.
    def outbreak_crawl(self):
        pathogentags = (tag for tag in outbreaksoup.find_all('b') if
                        isTag(tag) and tag.a)
        for tag in pathogentags:
            pathogen = tag.string
            ul = tag.next_sibling.next_sibling.next_sibling
            outbreaks = (desc for desc in ul.descendants if isTag(desc))
            for tag in outbreaks:
                if tag.name == "b":
                    year = tag.contents
                elif tag.name == "a":
                    location = tag.contents
                    url = tag['href']
                    pathid = re.search('[0-9]{5}', url).group()
                    locid = re.search('G[0-9]{2,3}', url).group()
                    self.pathogens.append(pathogen)
                    self.years.append(year)
                    self.locations.append(location)
                    self.urls.append(url)
                    self.pathids.append(pathid)
                    self.locids.append(locid)

    def print_all(self):
        for i in zip(self.pathogens, self.years, self.locations, self.urls, self.pathids, self.locids):
            print i




# Writes out all the data for a particular pathogen.
def write_pathogen_data():
    pathogenzip = zip(pathogen.years, pathogen.locations, pathogen.urls,
                      pathogen.pids, pathogen.lids)
    for i in pathogenzip:
        print pathogen.name, i

# pdb.set_trace()

if __name__ == '__main__':
    outbreaks = OutbreakData()
    outbreaks.outbreak_crawl()
    outbreaks.print_all()