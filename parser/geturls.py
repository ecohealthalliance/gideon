import csv
import lxml
from bs4 import BeautifulSoup
import os

# Create a subclass of HTMLParser 
class outbreak_html_parser(HTMLParser):
    def 