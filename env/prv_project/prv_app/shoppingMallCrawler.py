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

def findnum(strnum):
    for i in range(0, len(strnum)) :
        if strnum[i].isdigit() == True :
            return strnum[i]
#문자열중 숫자 찾는 함수

def search_shop_review(URL):
    url = URL
    #print(URL)

    driver = webdriver.Chrome('C:/Python_basic/env/prv_project/prv_app/chromedriver')
    #driver = webdriver.PhantomJS('/Users\/kddn/Documents/crawling/phantomjs-2.1.1-windows/bin/phantomjs') #판다스 사용할 경우 사용
    driver.implicitly_wait(3)
 
    # url에 접근한다.
    driver.get(url)
    #driver.find_element_by_xpath("//a[@data-maintarget='#vip_tab_comment']").click() #xpath 테스트
    driver.find_element_by_id("tap_moving_2").click()  
    sleep(1)
    
    # 3. 댓글 페이지 html 구조 긁어오기
    page = driver.page_source # 페이지의 elements모두 가져오기
    source = BeautifulSoup(page,'html.parser', from_encoding='utf-8') # 한글이 있기때문에 encoding 해줌  #[from_encoding='utf-8생략 가능]
    #print(source)
    
    # 페이지수 읽어오기 
    try:#ok
        page_num = source.find('div',{'class':'box__page-jump'}).find('em',{'class':'text'}).get_text()    #페이지 부분을 str 형태로 변환
        page_num=int(page_num) #str 을 int형으로 변환 

    except:
        page_num=1;#1페이지 일경우 1로 지정
    
    print(page_num)
    
    all_reviews=[]
    positive_reviews=[]
    negative_reviews=[]
    
    positive = 4    #defualt 값
    negative = 3    #defualt 값
    
    #페이지 수만큼 반복
    try:
        for numPage in range(1,page_num):
            # 4. 네티즌 댓글부분(태그 , {속성명: 속성값})   
            page = driver.page_source
            source = BeautifulSoup(page,'html.parser',from_encoding='utf-8')

            all_review = source.find('ul',{'clss','list__review'}).findAll('div',{'class':'box__content'})     #내용 추출
            #print(all_review)
            sleep(1)

            #전체 긍정 부정 리스트 추가
            for review in all_review:
                all_reviews.append(review.find('p',{'class':'text'}).get_text().strip().replace('\n','').replace('\t','').replace('\r',''))

                star = review.find('span',{'class':'for-a11y'}).text  #변수에 별점 내용 저장 
                star = int(findnum(star)) #내용중 findnum함수를 이용해 숫자를 찾아낸후 그것은 int형으로 저장
                #print(type(star))

                if(star >= positive):#긍정 부분 수집
                    positive_reviews.append(review.find('p',{'class':'text'}).get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
                if(star <= negative):#부정 부분 수집
                    negative_reviews.append(review.find('p',{'class':'text'}).get_text().strip().replace('\n','').replace('\t','').replace('\r',''))

            if(page_num>numPage):   #다음페이지 이동 조건 (전체 페이지보다 현제 페이지가 작을 경우)
                driver.find_element_by_xpath("//a[@class='link__page-move link__page-next']").click()  #다음페이지 이동
    
    except: #리뷰 내용 없음 별점만 해당 그 뒤페이지로도 쭉이기 때문에 전체 반복문 빠져나옴
        pass
    
    driver.close()  #드라이버 종료
    #print(all_reviews,positive_reviews,negative_reviews)

    # 텍스트파일에 댓글 저장하기
    file_a = open("shoppingMall_all.txt",'w+',encoding='utf-8')
    file_p = open("shoppingMall_pos.txt",'w+',encoding='utf-8')
    file_n = open("shoppingMall_neg.txt",'w+',encoding='utf-8')
    
    #전체 긍정 부정 리스트에서 읽어들여 텍스트 생성
    for review in all_reviews:
        file_a.write(review+'\n')
    for review in positive_reviews:
        file_p.write(review+'\n')
    for review in negative_reviews:
        file_n.write(review+'\n')

    file_a.close()
    file_p.close()
    file_n.close()