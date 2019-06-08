# 1. 웹크롤링에 필요한 모듈 호출
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains  #contril click in selenium
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석
from time import sleep
from . import splitSent
from urllib.request import urlopen 
import requests
import os
def search_shop_review(URL):
    url = URL
    #print(URL)

    driver = webdriver.Chrome('C:/Python_basic/env/prv_project/prv_app/chromedriver')
    #driver = webdriver.PhantomJS('/Users\/kddn/Documents/crawling/phantomjs-2.1.1-windows/bin/phantomjs') #판다스 사용할 경우 사용
    driver.implicitly_wait(3)
 
    # url에 접근한다.
    driver.get(url)
    #driver.find_element_by_xpath("//a[@data-maintarget='#vip_tab_comment']").click() #xpath 테스트
    driver.find_element_by_id("tap_moving_2").click()  #
    sleep(1)

    #iframe 주소로 변환 
    iframe = driver.find_element_by_id("iframeItemTalk")
    driver.switch_to.frame(iframe)
    #print(iframe)
    iframe2 = driver.find_element_by_id("ifFeedbackSecondList")
    driver.switch_to.frame(iframe2)
    #print(iframe2)

    #전체 버튼 클릭
    element = driver.find_element_by_id("btnPhotoViewYN_N")

    sleep(1)
    #새로운 텝 열기 control click
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(element) \
        .key_up(Keys.CONTROL) \
        .perform()

    sleep(1) # Pause to allow you to inspect the browser.

    #드라이버 위치를 신규 텝으로 전환
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)

    page = driver.page_source # 페이지의 elements모두 가져오기
    #print(html) #새 패이지의 element가 맞는지 확인 코드

    # 3. 댓글 페이지 html 구조 긁어오기
    source = BeautifulSoup(page,'html.parser', from_encoding='utf-8') # 한글이 있기때문에 encoding 해줌  #[from_encoding='utf-8생략 가능]
    #print(source)

    # 페이지수 읽어오기 
    page_num = source.find('div',{'class':'pagination pagination-interval'}).find('span',{'class':'num'}).get_text()    #페이지 부분을 str 형태로 변환
    page_num=int(page_num) #str 을 int형으로 변환 

    all_reviews=[]
    positive_reviews=[]
    negative_reviews=[]

    #페이지 수만큼 반복
    for numPage in range(1,page_num+1):
        # 4. 네티즌 댓글부분(태그 , {속성명: 속성값})   
        page = driver.page_source
        source = BeautifulSoup(page,'html.parser',from_encoding='utf-8')

        #reviews_title = revies_table.findAll('strong') #제목 추출 수정필요
        all_review = source.find('tbody').findAll('tr')      #내용 추출
        sleep(1)
    
        #전체 긍정 부정 리스트 추가
        for i in all_review:
            all_reviews.append(i.findAll('a')[0].get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
            all_reviews.append(i.findAll('a')[1].get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
        
            if(i.find('span',{'class':'badge-satisfaction badge-satisfaction-good'})):
                positive_reviews.append(i.findAll('a')[0].get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
                positive_reviews.append(i.findAll('a')[1].get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
        
            if(i.find('span',{'class':'badge-satisfaction badge-satisfaction-bad'})):
                negative_reviews.append(i.findAll('a')[0].get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
                negative_reviews.append(i.findAll('a')[1].get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
    
        if(page_num>numPage):
            driver.find_element_by_xpath("//a[@class='next']").click() #다음페이지 이동
    

    # 텍스트파일에 댓글 저장하기
    file_a = open("shoppingMall_all.txt",'w+',encoding='utf-8')
    file_p = open("shoppingMall_pos.txt",'w+',encoding='utf-8')
    file_n = open("shoppingMall_neg.txt",'w+',encoding='utf-8')
    
    for review in all_reviews:
        file_a.write(review+'\n')
    for review in positive_reviews:
        file_p.write(review+'\n')
    for review in negative_reviews:
        file_n.write(review+'\n')

    file_a.close()
    file_p.close()
    file_n.close()

    file_a = open("shoppingMall_all.txt",'r',encoding='utf-8')
    text_all = file_a.read() 
    splitSent.get_tags_all(text_all, 100)
    file_a.close()

    file_p = open("shoppingMall_pos.txt",'r',encoding='utf-8')
    try:
        text_pos = file_p.read()
        splitSent.get_tags_pos(text_pos, 100)
    except:
        file_p.close()

    file_n = open("shoppingMall_neg.txt",'r',encoding='utf-8')
    try:
        text_neg = file_n.read()
        splitSent.get_tags_neg(text_neg, 100)
        file_n.close()
    except:
        file_n.close()
#남은  부분
##영화와 사이트 class(매서드)로 구분 만들어줘야함