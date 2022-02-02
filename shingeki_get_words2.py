# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "https://meigen.keiziban-jp.com/%E9%80%B2%E6%92%83%E3%81%AE%E5%B7%A8%E4%BA%BA"
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
#print(soup)
linkset = soup.findAll('div', class_ = 'description')
for i in linkset:
    print(i.text)