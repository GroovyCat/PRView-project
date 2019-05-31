## 1. 웹크롤링을 위한 웹드라이버 응용 2
from selenium import webdriver
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains #contril click in selenium
import math #math 모듈을 먼저 import해야 한다.
from time import sleep 
 
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