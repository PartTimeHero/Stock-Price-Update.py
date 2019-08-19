# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 21:13:35 2019

@author: Ary
"""
# imports Beautiful Soup module
import bs4

# imports requests 
import requests

# imports Beautiful Soup
from bs4 import BeautifulSoup

# loop that grabs the price from Yahoo page element, then returns price
def parsePrice():
    r=requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup=bs4.BeautifulSoup(r.text, "xml")
    price=soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

# always returns current stock price in the string parsePrice
while True:
    print('the current price: '+str(parsePrice()))
