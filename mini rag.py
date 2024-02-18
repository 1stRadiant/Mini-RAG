import requests
import urllib.parse
from bs4 import BeautifulSoup

query = 'Who is Robert Downey Jr'
encodedString = urllib.parse.quote(query)

URL = "https://duckduckgo.com/?q=\%s:"+encodedString


import sys
from selenium import webdriver

sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome(options=options)
wd.get(URL)

html_content = wd.page_source

soup = BeautifulSoup(html_content, 'html.parser')
text_content = soup.get_text()

print(text_content)
