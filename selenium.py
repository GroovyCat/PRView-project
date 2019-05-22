# 1. 웹크롤링에 필요한 웹드라이버 모듈 호출
from selenium import webdriver
import time
 
driver = webdriver.Chrome('/Users/wkddn/Documents/crawling/ChromeDriver 74.0.3729.6/chromedriver')
#driver = webdriver.PhantomJS('/Users\/kddn/Documents/crawling/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(3)
# url에 접근한다.
url='http://itempage3.auction.co.kr/DetailView.aspx?itemno=A531834351'

driver.get(url)
driver.find_element_by_xpath("//a[@data-maintarget='#vip_tab_comment']").click()

html = driver.page_source # 페이지의 elements모두 가져오기
#print(html)