from __future__ import print_function
import os
import csv
import gidcommon as gc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import numpy as np
import pandas as pd

os.chdir(gc.datadir)

email = 'chmura@ecohealthalliance.org'
password = '1potato2potato'

driver = webdriver.Firefox()
driver.get("http://www.gideononline.com")
sleep(random.lognormvariate(1.5,0.5))
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(password, Keys.RETURN)
sleep(random.lognormvariate(2.5,0.5))

# Set up our dict of series
diseases_by_country = {}

driver.get("http://web.gideononline.com/web/epidemiology/")
country_menu = driver.find_element_by_name('country')
countries = map(lambda x:x.text, country_menu.find_elements_by_tag_name('option'))

for country in countries:
    print(country)
    driver.find_element_by_xpath("//*[contains(text(), '" +
                                 country +
                                 "')]").click()
    print("Sleeping...")
    sleep(random.lognormvariate(1.7,0.8))
    menulayer = driver.find_element_by_id('menuLayer')
    diseases = menulayer.find_elements_by_tag_name('a')
    diseases = map(lambda x: x.text, diseases)
    print(diseases)

    print("Making a series for this country")
    diseases = pd.Series(1., index=diseases)

    print("Assigning that series to the diseases_by_country dict.")
    diseases_by_country[country] = diseases

    print("Sleeping again...")
    sleep(random.lognormvariate(1,0.5))

diseases_by_country = pd.DataFrame(diseases_by_country)

diseases_by_country

outfile = os.path.expanduser("~/Desktop/diseases_by_country.csv")

diseases_by_country.to_csv(outfile)