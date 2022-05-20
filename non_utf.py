# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:14:19 2022

@author: DennisLin
"""

import requests
from bs4 import BeautifulSoup

resp = requests.get("https://zhidao.baidu.com/question/48795122.html")
resp.encoding='gbk'
soup = BeautifulSoup(resp.text, "html.parser")
title = soup.find('span', 'ask-title')
print(title.text)