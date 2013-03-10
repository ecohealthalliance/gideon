import os
import csv
import gidcommon as gc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


os.chdir(gc.datadir)
urls = open(gc.outdir + 'gideon-dl-urls-test2.csv')

urlreader = csv.reader(urls)
urlreader.next()

email = raw_input('Enter email address: ')
password = raw_input('Enter password: ')

driver = webdriver.Firefox()
driver.get("http://www.gideononline.com")
sleep(random.lognormvariate(1.5,0.5))
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(password, Keys.RETURN)
sleep(random.lognormvariate(1.5,0.5))

for row in urlreader:
    pathogen = row[0]
    country = row[1]
    url = row[2]
    while True:
        try:
            driver.get(url)
            driver.find_element_by_id('timeout_box')
            break
        except:
            print "Page not correctly loaded, trying again."
    f = open(gc.indir + "outbreaks/" + pathogen + "_" + country + ".html", 'w+')
    src = driver.page_source
    f.write(src.encode('utf8'))
    f.close()
    print "Saved: " + gc.indir + "outbreaks/" + pathogen + "_" + country + \
          ".html"
    sleep(random.lognormvariate(1.5,0.5))

driver.close()