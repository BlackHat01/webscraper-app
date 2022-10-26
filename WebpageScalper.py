# Open Libraries

from platform import python_version
from telnetlib import STATUS

from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

# Set browser to Chrome

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# Create lists to store data


# Open CR

import webbrowser
CR_LINK = input("Paste CR Link here: ")
webbrowser.open(CR_LINK, new=1)



content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
name=a.find('div', attrs={'class':'_3wU53n'})
price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text) 