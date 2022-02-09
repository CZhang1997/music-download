#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:41:02 2019

@author: churongzhang
"""
import re
import requests
from bs4 import BeautifulSoup as BS
import sys

req = requests.Session()

def getFirstURL(song_name):
    url = "https://www.youtube.com/results?search_query={}".format(song_name)
    text = req.get(url).text
    url2 = re.search("watch?v=", str(text))
    print(url2.group(1))
    

if __name__ == "__main__":
    for i in range(24):
        print(i + 2)