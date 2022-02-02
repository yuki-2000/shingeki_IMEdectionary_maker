# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

response = requests.get("https://meigen.dancing-doll.com/attack-on-titan/")
soup = BeautifulSoup(response.content,'lxml')
link_body = soup.find("section", class_ ="ss2-wrap")
aa = link_body.findAll('a')


urls=[]

for j in aa:
    urls.append(j.get("href"))

texts = []
for url in urls:   


    response = requests.get(url)
    soup = BeautifulSoup(response.content,'lxml')
    linkset = soup.findAll('span', class_ = 'color-saying')

    for i in linkset:
        print(i.text)
        b = i.text.split("「")
        for bb in b:
            texts.append(bb.split("」")[0])


texts = [x for x in texts if (x !="" and x !=" " and x !="　")]


import pyperclip
pyperclip.copy("\n".join(texts))