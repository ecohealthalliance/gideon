import sys
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium import selenium

driver = webdriver.Firefox()
driver.get("http://www.gideononline.com")
driver.find_element_by_name("email").send_keys("toph.allen@yahoo.com")
driver.find_element_by_name("password").send_keys("pwgideon", Keys.RETURN)

# sel = selenium('localhost', 4444, '*firefox', 'http://www.google.com')
# sel.start()
# sel.open("http://www.gideononline.com")
# sel.type("email","toph.allen@yahoo.com")
# sel.type("password","pwgideon")