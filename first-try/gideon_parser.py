# we open our files
gdump = open("gideon_dump.txt", 'r+')
gdatabase = open("gdatabase.csv", 'w')

# get end of file for while loop below, then rewind.
print gdump.read()
end_pos = gdump.tell()
gdump.seek(0)
curr_pos = gdump.tell()

# tests to see if we're on a line starting with a year
def numtest():
    global curr_pos
    curr_pos = gdump.tell()
    first4 = gdump.read(4)
    gdump.seek(curr_pos)
    isnum = first4.isdigit()
    return isnum

# set global pathogen var to the current line
def get_pathogen():
    global pathogen
    pathogen = gdump.readline()

# set global year var to first 4 chars of line, advance two chars
def get_year():
    global year
    year = gdump.read(4)
    gdump.seek(2, 1)

# set global countries var to list of countries
def get_countries():
    country_line = gdump.readline()
    global countries
    countries = country_line.split(', ')

# the main loop; tests to see if we're on a year line, sets pathogen, year and country vars, and then prints them and writes them to the output file.
while end_pos > gdump.tell():
    if numtest() == False:
        get_pathogen()
    else:
        get_year()
        get_countries() 
        for country in countries:
            print pathogen.rstrip('\r\n') + ","  +str(year) + "," + country.rstrip('\r\n')
            line = pathogen.rstrip('\r\n') + ","  +str(year) + "," + country.rstrip('\r\n') + "\n"
            gdatabase.write(line)
        

# This is just a test loop
#while end_pos > gdump.tell():
#    print numtest()
#    print "The current position is " + str(gdump.tell()) + "."
#    print gdump.readline()

gdump.close()
gdatabase.close()