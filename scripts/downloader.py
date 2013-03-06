import os
import csv
import gidcommon as gc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.chdir(gc.datadir)
urls = open(gc.outdir + 'gideon-dl-urls-test.csv')

urlreader = csv.reader(urls)
urlreader.next()

email = ''
password = ''

driver = webdriver.Firefox()
# driver.get("http://www.gideononline.com")
# driver.find_element_by_name("email").send_keys(email)
# driver.find_element_by_name("password").send_keys(password, Keys.RETURN)

for row in urlreader:
    pathogen = row[0]
    country = row[1]
    url = row[2]
    driver.get(url)
    f = open(gc.indir + "outbreaks/" + pathogen + "_" + country + ".html", 'w+')
    src = driver.page_source
    f.write(src.encode('utf8'))
    f.close()

driver.close()