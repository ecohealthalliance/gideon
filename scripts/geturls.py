import sys
import os # Use os.chdir to open file
import csv
import bs4
import lxml
import re
import pdb

# Create csv readers


datadir = "../data/"
indir = "raw/"
outdir = "processed/"
infile = "gideon-outbreaks-only.html"
outfile = "gideon-outbreaks-csv2.csv"


# Returns true if an item is a bs4 tag.
def isTag(item):
    if isinstance(item, bs4.element.Tag):
        return True
    return False

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
            # ul = tag.next_sibling.next_sibling.next_sibling
            for sib in tag.next_siblings:
                if isTag(sib) and sib.name == 'ul':
                    ul = sib
                    break
            outbreaks = (desc for desc in ul.descendants if isTag(desc))
            for tag in outbreaks:
                if tag.name == "b":
                    year = tag.string
                elif tag.name == "a":
                    location = tag.string
                    url = tag['href']
                    pathid = re.search('[0-9]{5}', url).group()
                    locid = re.search('G[0-9]{2,3}', url).group()
                    self.pathogens.append(str(pathogen))
                    self.years.append(str(year))
                    self.locations.append(str(location))
                    self.urls.append(url)
                    self.pathids.append(pathid)
                    self.locids.append(locid)

    def print_current(self):
        for i in zip(self.pathogens, self.years, self.locations, self.pathids,
                     self.locids, self.urls):
            print i


if __name__ == '__main__':
    os.chdir(datadir)
    outbreakhtml = open(indir + infile, 'r')
    outbreaksoup = bs4.BeautifulSoup(outbreakhtml, "lxml")
    outbreakhtml.close()
    outbreaks = OutbreakData()
    outbreaks.outbreak_crawl()
    # outbreaks.print_current()
    outbreakcsv = open(outdir + outfile, 'w+')
    outbreakwriter = csv.writer(outbreakcsv)
    headers = ['pathogen', 'year', 'location', 'path_id', 'loc_id', 'url']
    outbreakwriter.writerow(headers)
    for row in zip(outbreaks.pathogens, outbreaks.years, outbreaks.locations,
                   outbreaks.pathids, outbreaks.locids, outbreaks.urls):
        outbreakwriter.writerow(row)
    outbreakcsv.close()