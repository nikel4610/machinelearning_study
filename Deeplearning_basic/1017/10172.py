from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://glee-glee.com/'
html = req.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

# 상품명 추출
title = soup.find_all('span', {'class':'name'})
for i in title:
    print(i.text)
