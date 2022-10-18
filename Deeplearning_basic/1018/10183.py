import os
import sys
import urllib.request
import json

client_id = json.loads(open('D:/vsc_project/machinelearning_study/api.json').read())['client_id']
client_secret = json.loads(open('D:/vsc_project/machinelearning_study/api.json').read())['client_secret']

encText = urllib.parse.quote("인공지능")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=40&start=1&sort=date"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if rescode==200:
    response_body = response.read()
else:
    print("Error Code:" + rescode)

type(eval(response_body.decode('utf-8')))
rData = eval(response_body.decode('utf-8'))
print(len( rData['items'] ))

# 링크만 뽑아오기
for i in range(len( rData['items'] )):
    print(rData['items'][i]['link'])

