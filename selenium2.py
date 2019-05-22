## 1. 웹크롤링을 위한 웹드라이버 응용 2
from selenium import webdriver
import time
 
driver = webdriver.Chrome('/Users/wkddn/Documents/crawling/ChromeDriver 74.0.3729.6/chromedriver')
#driver = webdriver.PhantomJS('/Users\/kddn/Documents/crawling/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://www.naver.com/')
#웹드라이버를 사용하여 (검색과 사이트 이동(click))
elem=driver.find_element_by_name("query").send_keys('뺑반')
driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click() 
#신규텝으로 이동 / 드라이버는 위치는 기존유지
driver.find_element_by_xpath('//*[@id="_au_movie_info"]/div[2]/dl[1]/dd[4]/a').click() 
#드라이버 위치를 신규 텝으로 전환
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)
html = driver.page_source # 페이지의 elements모두 가져오기
print(html) #새 패이지의 element가 맞는지 확인 코드

#이후 BeautifulSoup을 이용하여 크롤링 + page 텝의 리뷰수를 긁어와 계산하여 끝페이지까지