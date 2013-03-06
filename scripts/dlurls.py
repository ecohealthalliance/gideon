import sys
import os
import csv
import gidcommon as gc

os.chdir(gc.datadir)
gidcsv = open(gc.outdir + 'gideon-outbreaks-csv.csv')
urlcsv = open(gc.outdir + 'gideon-dl-urls.csv', 'w+')

# These are the fragments from which the urls will be composited.
urlfrag1 = 'http://web.gideononline.com/web/epidemiology/country_info.php?source=&country_id='
urlfrag2 = '&disease_id='

reader = csv.reader(gidcsv)
writer = csv.writer(urlcsv)

# Create a new header row and skip the old one.
headers = ['pathogen', 'country', 'url']
writer.writerow(headers)
reader.next()

# Iterate through csv, pulling out country and pathogen and creating url.
for row in reader:
    pathogen = row[0]
    country = row[2]
    newurl = (urlfrag1 + str(row[4]) + urlfrag2 + str(row[3]))
    newrow = [pathogen, country, newurl]
    writer.writerow(newrow)

gidcsv.close()
urlcsv.close()