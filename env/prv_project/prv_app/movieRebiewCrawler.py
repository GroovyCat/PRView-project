'''

 <영화 제목을 입력 받아 영화 리뷰(전체, 긍정, 부정)으로 나누어 텍스트를 생성하는 프로그램> 
selenium 함수의 기능과 BeautifulSoup을 이용하여 페이지를 이동하며 원하는 값을 스크레핑 하고 방법으로는
requests 함수를 통해 url에서 응답메시지를 읽어온후에 스크래핑 작업을 수행 그리고 빠른 동작을 위하여 
multipocessing 을 모듈의 함수중 하나인 pool함수 사용합니다. 기본적으로는 pool.map() 인자는 하나 이나 
partial, contextlib의 contextmanager 함수를 활용 하여 인자값을 2개 받아 작동 후 최종 결과 값을 text값으로 
출력해주는 해주며 종료되는 프로그램 입니다.

'''

from selenium import webdriver #  웹크롤링을 위한 웹드라이버
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석
# selenium 마우스 컨트롤 기능 ex control + click 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math #math 수식을 위한 모듈
from time import sleep, time #time함수
#서버 접근 허용을 위해 사용 
from urllib.request import urlopen 
import requests 
#from . import splitSent 
#멀티프로세싱을 위한 모듈
import multiprocessing  
from functools import partial
from contextlib import contextmanager


# 영화명을 입력받아  [영화 페이지 url, 전체 페이지 숫자] 리턴 함수
def movieUrl(name):
    movieName = name

    #헤드 리스 모드 사용할시  (30번 라인 지우고 주석 헤제) 
    # options = webdriver.ChromeOptions() #크롬 옵션
    #options.add_argument('headless')    #headless 모드
    #options.add_argument('window-size=1920*1080')
    #options.add_argument("disable-gpu")
    #options.add_argument("--disable-gpu") #오류가 생길시
    #driver = webdriver.Chrome(C:/Python_basic/env/prv_project/prv_app/chromedriver', chrome_options=options)
    
    driver = webdriver.Chrome('C:/Python_basic/env/prv_project/prv_app/chromedriver')
    driver.implicitly_wait(2)
    # url에 접근한다.

    driver.get('https://www.naver.com/') #네이버로 이동
    #웹드라이버를 사용하여 (검색과 사이트 이동(click))

    elem=driver.find_element_by_name("query").send_keys(movieName) #검색창에 입력 값 검색
    driver.find_element_by_xpath('//*[@id="search_btn"]').click()  #검색 클릭
    
    driver.find_element_by_xpath("//a[@class='sh_movie_link']").click()  #영화사이트 이동
    #신규텝으로 이동 / 드라이버는 위치는 기존유지

    #드라이버 위치를 신규 텝으로 전환
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)
    driver.find_element_by_xpath("//a[@class='tab05_off']").click() #영화 리뷰 페이지 1

    #사이트 이동을 위해 iframe의 주소 받아옴 
    iframe = driver.find_element_by_id("pointAfterListIframe") #id로 iframe 값을 찾음
    driver.switch_to.frame(iframe) #변환해줌

    element =driver.find_element_by_xpath("//a[@id='pagerTagAnchor1']") #전체 리뷰 페이지

    #cotrol + cllick 기능 함수
    ActionChains(driver) \
        .key_down(Keys.CONTROL) \
        .click(element) \
        .key_up(Keys.CONTROL) \
        .perform()
    
    sleep(1) 

    #드라이버 위치를 신규 텝으로 전환
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)

    html = driver.page_source # 페이지의 elements모두 가져오기
    #print(html) #새 패이지의 element가 맞는지 확인 코드

    # 3. 댓글 페이지 html 구조 긁어오기
    source = BeautifulSoup(html,'html.parser',from_encoding='utf-8') # 한글이 있기때문에 encoding 해줌

    # 페이지수 읽어오기 
    page_num = source.find('strong',{'class':'total'}).findAll('em')[1].get_text() #총 평가수
    page_num=(int(page_num.replace(',','')))/10 #str 을 int형으로 변환  / 읽어온 텍스트중 ,표시를 공백으로 바꿔줌
    page_num=math.ceil(page_num) #math 모듈의 올림 함수

    if(page_num>1000):
        page_num=1000
        #print(page_num)

    movie_url = driver.current_url  #영화 리뷰 사이트 url 받아오기  (현제 url 받아오는 함수 사용)
    movie_url= movie_url.replace('&page=1', '&page={}') #replace함수를 사용해 url을 반복문에 사용하기 좋게 바꿔주기
    
    driver.close()  #드라이버 종료

    return movie_url, page_num  #영화 페이지 url, 전체 페이지 숫자 


#멀티 프로세싱할 함수 pool을 이용해 작동 map함수 인자값이 하나지만 해결 파이썬 3.6이상부터 해결방법으로 해결
#페이지와 영화 url부분을 받아 멀티프로세싱 동작 실행
def movieCrawler(start,Mpage):
    all_movie_reviews=[]
    positive_movie_reviews=[]
    negative_movie_reviews=[]

    positive = 7    #defualt 값
    negative = 4    #defualt 값

    ##페이지 수만큼 반복
    for i in range(1, 15):
        url = movieUrl.format(i)
        webpage = urlopen(url)
        source = BeautifulSoup(webpage,'html.parser',from_encoding='utf-8')
        reviews=source.find('div',{'class': 'score_result'}).findAll('li')
   
        sleep(1)
        #전체 내용 담기
        for review in reviews:
            #전체 수집
            all_movie_reviews.append(review.p.get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
        
            if(int(review.em.text) >= positive):#긍정 부분 수집
                positive_movie_reviews.append(review.p.get_text().strip().replace('\n','').replace('\t','').replace('\r',''))
       
            if(int(review.em.text) <= negative):#부정 부분 수집                                  
                negative_movie_reviews.append(review.p.get_text().strip().replace('\n','').replace('\t','').replace('\r',''))

        #if(page_num>numPage):
            #driver.find_element_by_xpath("//a[@class='next']").click() #다음페이지 이동

        ## 텍스트파일에 댓글 저장하기
        #전체, 긍정, 부정 순서
    file_a = open('movie_all.txt', 'w+', encoding='utf-8') 
    file_p = open('movie_pos.txt', 'w+', encoding='utf-8')
    file_n = open('movie_neg.txt', 'w+', encoding='utf-8')

    for review in all_movie_reviews:
        file_a.write(review+'\n')

    for review in positive_movie_reviews:
        file_p.write(review+'\n')

    for review in negative_movie_reviews:
        file_n.write(review+'\n')
    
    file_a.close()
    file_p.close()
    file_n.close()