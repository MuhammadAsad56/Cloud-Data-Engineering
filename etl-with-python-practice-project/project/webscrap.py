
from io import StringIO  # json format ko readable format me karne ke liye
import requests # url hit karne ke liye 
from bs4 import BeautifulSoup # html ko saaf karne ke liye
import pandas as pd
import sqlite3
from datetime import datetime

url = 'https://web.archive.org/web/20230908091635/https://www.pakwheels.com/used-cars/karachi/24857'
soup = BeautifulSoup(requests.get(url).text, "html.parser")
table_attribs = "Sort By:"

table = soup.find("ul", class_="line-unstyled search-results search-results-mid next-prev car-search-result").find_all("li", recursive=F)
print(table)
    