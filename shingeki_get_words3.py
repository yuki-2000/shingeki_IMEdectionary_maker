# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "https://www.underwater-festival.com/00063-2/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
#print(soup)
linkset = soup.findAll('blockquote', class_ = 'wp-block-quote')
for i in linkset:
    print(i.find("p").text)