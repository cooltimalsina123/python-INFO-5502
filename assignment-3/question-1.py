import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import csv

url_page = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

webpage = urllib.request.urlopen(url_page)
soup = BeautifulSoup(webpage)
print(soup.prettify())

