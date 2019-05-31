## 1. 웹크롤링을 위한 웹드라이버 응용 2
from selenium import webdriver
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains #contril click in selenium
import math #math 모듈을 먼저 import해야 한다.
from time import sleep
from urllib.request import urlopen # 특정 웹서버에 접근
import requests #서버 접근 허용을 위해 사용 
 
driver = webdriver.Chrome('/Users/wkddn/Documents/crawling/ChromeDriver 74.0.3729.6/chromedriver')
#driver = webdriver.PhantomJS('/Users\/kddn/Documents/crawling/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(3)
# url에 접근한다.

driver.get('https://www.naver.com/') #네이버로 이동
#웹드라이버를 사용하여 (검색과 사이트 이동(click))

elem=driver.find_element_by_name("query").send_keys('악인전') #검색창에 악인전 검색
driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click() 
#신규텝으로 이동 / 드라이버는 위치는 기존유지

driver.find_element_by_xpath("//a[@class='sh_movie_link']").click() 

#드라이버 위치를 신규 텝으로 전환
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)
driver.find_element_by_xpath("//a[@class='tab05_off']").click() #영화 리뷰 페이지 1

#사이트 이동을 위해 iframe의 주소 받아옴 
iframe = driver.find_element_by_id("pointAfterListIframe") #id로 iframe 값을 찾음
driver.switch_to.frame(iframe) #변환해줌

element =driver.find_element_by_xpath("//a[@id='pagerTagAnchor1']") #리뷰 페이지

ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .click(element) \
    .key_up(Keys.CONTROL) \
    .perform()

sleep(3) 

#드라이버 위치를 신규 텝으로 전환
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)

html = driver.page_source # 페이지의 elements모두 가져오기
#print(html) #새 패이지의 element가 맞는지 확인 코드

# 3. 댓글 페이지 html 구조 긁어오기
source = BeautifulSoup(html,'html.parser',from_encoding='utf-8') # 한글이 있기때문에 encoding 해줌
#print(source)

# 페이지수 읽어오기 
page_num = source.find('strong',{'class':'total'}).findAll('em')[1].get_text() #총 평가수
page_num=(int(page_num.replace(',','')))/10 #str 을 int형으로 변환 읽어온 텍스트중 ,표시를 공백으로 바꿔줌
page_num=math.ceil(page_num) #올림
#print(page_num)

if(page_num>1000):
    page_num=1000
#print(page_num)

movieUrl = driver.current_url  #영화 리뷰 사이트 url 받아오기  (현제 url 받아오는 함수 사용)
movieUrl= movieUrl.replace('&page=1', '&page={}') #replace함수를 사용해 url을 반복문에 사용하기 좋게 바꿔주기

movie_reviews=[]
#페이지 수만큼 반복
for i in range(1,page_num+1):
    url = movieUrl.format(i)
    webpage = urlopen(url)
    source = BeautifulSoup(webpage,'html.parser',from_encoding='utf-8')
    reviews = source.find('div',{'class': 'score_result'}).findAll('li')
    time.sleep(1)
    for review in reviews:
        movie_reviews.append(review.p.get_text().strip().replace('\n','').replace('\t','').replace('\r',''))

# 텍스트파일에 댓글 저장하기
file = open('movie_b.txt','w',encoding='utf-8')

for review in movie_reviews:
    file.write(review+'\n')

file.close()
print("end")