import requests
import lxml
from bs4 import BeautifulSoup

#다음은 네이버 뉴스의 헤드라이트를 스크래핑 하는 코드입니다. ()안에 알맞은 코드를 완성하세요.
#1번 requests를 활용하여 https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100 에 접속하고
#2번 requests헤더에 {'User-Agent':'Mozilla/5.0'} 를 추가하세요.
html = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100', headers={'User-Agent':'Mozilla/5.0'})
#3번 Bearutifulsoup객체를 만들고 lxml 파서를 생성하세요.
bs = BeautifulSoup(html.text, 'lxml')

#4번 ul태그로 시작하고
#5번 class속성이 section_list_ranking_press 인것을 찾는 코드를 작성하세요.
result = bs.find('ul', class_ = 'section_list_ranking_press')

#6번~9번 result에서 tag가 div이고 class속성이 list_text인것을 모두 찾는 코드를 완성하세요
result1 = result.find_all('div', class_ = 'list_text')
for temp in result1:
    print(temp.text) #10번 temp의 내용을 화면에 문자로 출력하는 코드를 완성하세요.

