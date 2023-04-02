# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import requests
from bs4 import BeautifulSoup
import jieba

url = 'https://news.163.com/'

#伪装成浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#取得网页的内容
response = requests.get(url, headers=headers)
#print(response)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
#调取网址
for link in soup.find_all('a'):
    print(link.get('href'))
