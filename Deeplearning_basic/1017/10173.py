from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver as wd

# url = 'https://ko.wikisource.org/wiki/%ED%95%98%EB%8A%98%EA%B3%BC_%EB%B0%94%EB%9E%8C%EA%B3%BC_%EB%B3%84%EA%B3%BC_%EC%8B%9C'
# html = req.urlopen(url)
# soup = BeautifulSoup(html, 'html.parser')
#
# poems = soup.select('#mw-content-text > div.mw-parser-output > ul')
# for i in poems:
#     print(i.text)

driver = wd.Edge(executable_path='D:/vsc_project/machinelearning_study/edgedriver_win64/msedgedriver.exe')
url = 'http://www.naver.com'
keyword = '파이썬'

driver.get(url)
element = driver.find_element_by_id('query')
element.send_keys(keyword)
element_Btn = driver.find_element_by_id('search_btn')
element_Btn.click()