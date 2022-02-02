# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

urls = ["https://animemanga33.com/archives/11714",
        "https://animemanga33.com/archives/23971",
        "https://animemanga33.com/archives/29688",
        "https://animemanga33.com/archives/29749",
        "https://animemanga33.com/archives/30060",
        "https://animemanga33.com/archives/17650",
        "https://animemanga33.com/archives/17653",
        "https://animemanga33.com/archives/17656",
        "https://animemanga33.com/archives/17659",
        "https://animemanga33.com/archives/17662",
        "https://animemanga33.com/archives/30062",
        "https://animemanga33.com/archives/30064",
        "https://animemanga33.com/archives/17789",
        "https://animemanga33.com/archives/17791",
        "https://animemanga33.com/archives/30066",
        "https://animemanga33.com/archives/17787",
        "https://animemanga33.com/archives/30068",
        "https://animemanga33.com/archives/30070",
        "https://animemanga33.com/archives/17675",
        "https://animemanga33.com/archives/17795",
        "https://animemanga33.com/archives/17793",
        "https://animemanga33.com/archives/30072",
        "https://animemanga33.com/archives/30074",
        "https://animemanga33.com/archives/30076",
        "https://animemanga33.com/archives/33832",]


texts = []
for url in urls:   


    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    #print(soup)
    #linkset = soup.findAll('', class_ = 'wp-block-quote')
    linkset = soup.findAll('p')

    for i in linkset:
        #print(i.text)
        a = i.text.split("(")[0]
        b = a.split("「")
        for bb in b:
            texts.append(bb.split("」")[0])


texts = [x for x in texts if (x !="" and x !=" " and x !="　")]


import pyperclip
pyperclip.copy("\n".join(texts))