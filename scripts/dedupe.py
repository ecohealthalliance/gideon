import os
import gidcommon as gc

os.chdir(gc.datadir)
infile = 'gideon-dl-urls.csv'
outfile = 'gideon-dl-urls-deduped.csv'

duped = open(gc.outdir + infile, 'r')
deduped = open(gc.outdir + outfile, 'w+')

oldrows = []
newrows = []

# Gather all rows from old file.
for row in duped:
    oldrows.append(row)

print "There are %s rows in the source file." %len(oldrows)

# Append unique rows to new file and also a list so we can count them.
for row in oldrows:
    if row not in newrows:
        newrows.append(row)
        deduped.write(row)

print "The deduped file has %s rows." %len(newrows)

duped.close()
deduped.close()