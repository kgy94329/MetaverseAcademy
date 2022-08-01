from contextlib import redirect_stderr
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def get_rgb(r, g, b):
    red = r
    green = g
    blue = b


#다음은 셀레니움과 BeautifulSoup를 이용하여 네이버 베스트셀러를 스크래핑 하는 코드입니다..
#다음 괄호안의 내용을 채워넣으세요.

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options= chrome_options)

# 크롬창을 최대로
driver.maximize_window()


driver.get('https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=rgb+%EC%83%89%EC%83%81%ED%91%9C&oquery=rgb+%EA%B3%84%EC%82%B0%EA%B8%B0&tqi=hWAT0wprvxZssk0ymRosssssta8-330866&acq=rgb&acr=2&qdt=0')

time.sleep(5)

# html코드 가져오기
html =  driver.page_source 

bs = BeautifulSoup(html, 'lxml')

red_input = bs.find('id' ,class_= 'input_rgbcode')


best_list = []
for temp in bookname:
    best_list.append(temp.text)

print(best_list)