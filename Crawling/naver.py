import os
import sys
import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

client_id = "t8DxU6OctYRLNs_7fIzt"
client_secret = "K_nH8Rr1WH"
encText = urllib.parse.quote("메타버스")

blogdescription = []
for i in range(10):
    #네이버 api를 이용하여 blogdescription에 1000개의 메타버스블로그 내용을 저장하는 코드를 완성하여 제출하세요.
    #실행시 [블로그1내용, 블로그2내용,.......블로그1000내용]와 같이 1000개의 블로그내용이 출력되어야합니다.
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=100&start=" + str((i*100)+1) # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_body = json.loads(response_body)
        resultdata = response_body['items']
        for temp in resultdata:
            blogdescription.append(temp['description'])
    else:
        print("Error Code:" + rescode)
print(blogdescription)


