'''

<url을 입력 받아 구매후기(전체, 긍정, 부정)으로 나누어 텍스트를 생성하는 프로그램> 
selenium 함수의 기능과 BeautifulSoup을 이용하여 페이지를 이동하며 원하는 값을 스크레핑 하고 방법으로는
페이지를 이동하며 각 페이지의 속성 값들을 읽어 판단하여 진행하고 페이지의 타입을 int형 str형으로 변환하여 
판단값으로 사용됩니다. 페이지를 selenium으로 이동하며 페이지를 BeautifulSoup으로 페이지 내용
을 생성하여 전체,긍정,부정 데이터 리스트를 생성하고 그값을 통해 텍스트에 저장하는 프로그램입니다.

'''

# 1. 웹크롤링에 필요한 모듈 호출
from selenium import webdriver #  웹크롤링을 위한 웹드라이버
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석
# selenium 마우스 컨트롤 기능 ex control + click 
from selenium.webdriver.common.action_chains import ActionChains  #contril click in selenium
from selenium.webdriver.common.keys import Keys
from time import sleep,time     #작동시간 체크, sleep기능 사용
#서버 접근 허용을 위해 사용 
from urllib.request import urlopen 
import requests
#
from . import splitSent
import os


#문자열중 숫자 찾는 함수
def findnum(strnum):
    for i in range(0, len(strnum)) :
        if strnum[i].isdigit() == True :
            return strnum[i]


def search_shop_review(URL):
    start_time = time() #시간 함수 시작시간
    url = URL

    #헤드 리스 모드 사용할시  (42번 라인 지우고 주석 헤제) 
    #options = webdriver.ChromeOptions() #크롬 옵션
    #options.add_argument('headless')    #headless 모드
    #options.add_argument('window-size=1920*1080')
    #options.add_argument("disable-gpu")
    #options.add_argument("--disable-gpu") #오류가 생길시
    #driver = webdriver.Chrome('C:/Python_basic/env/prv_project/prv_app/chromedriver', chrome_options=options)

    driver = webdriver.Chrome('C:/Python_basic/env/prv_project/prv_app/chromedriver')
    driver.implicitly_wait(2)
 
    # url에 접근한다.
    driver.get(url)
    #driver.find_element_by_xpath("//a[@data-maintarget='#vip_tab_comment']").click() #xpath 테스트
    driver.find_element_by_id("tap_moving_2").click()   #구매 후기 위치 클릭
    sleep(1)
    
    # 댓글 페이지 html 구조 긁어오기
    page = driver.page_source # 페이지의 elements모두 가져오기
    source = BeautifulSoup(page,'html.parser', from_encoding='utf-8') # 한글이 있기때문에 encoding 해줌  #[from_encoding='utf-8생략 가능]
    #print(source)
    
    # 페이지수 읽어오기 
    try:
        page_num = source.find('div',{'class':'box__page-jump'}).find('em',{'class':'text'}).get_text()    #페이지 부분을 str 형태로 변환
        page_num=int(page_num) #str 을 int형으로 변환 

    except: #1페이지 이상 없을 경우 실행문
        page_num=1;# 1페이지 일경우 1로 지정
    #print(page_num)
    
    #전체 긍정 부정 리스트 생성
    all_reviews=[]
    positive_reviews=[]
    negative_reviews=[]
    
    #긍정 부정 점수 // defualt 값 입력을 받아 사용할수는 있으나 개발 코스트로 인해 defult로 사용했읍니다.
    positive = 4    #defualt 값
    negative = 3    #defualt 값
    
    #리뷰 내용이 없을시 오류해결위한 try문
    try:  #페이지 수만큼 반복
        for numPage in range(1,page_num):
            # 현제 페이지 텍스트 page_source 와 BeautifulSoup 함수로 생성
            page = driver.page_source
            source = BeautifulSoup(page,'html.parser',from_encoding='utf-8')

            # 현제 페이지 리뷰 부분 BeautifulSoup 리스트 생성
            all_review = source.find('ul',{'clss','list__review'}).findAll('div',{'class':'box__content'})     #내용 추출 전체 리뷰.각 리뷰데이터
            #print(all_review)
            sleep(1)

            #위 추출 내용중 전체 긍정 부정 리스트 추가 반복문
            for review in all_review:
                #전체 리뷰 리스트에 추가
                all_reviews.append(review.find('p',{'class':'text'}).get_text().strip().replace('\n','').replace('\t','').replace('\r','')) #get_text 이상 부분은 텍스트로 변환 + 전처리

                #별점내용 읽어들여 숫자 값만 뽑아서 int형으로 변환
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

    #텍스트 파일 생성후 파일 종료
    file_a.close()
    file_p.close()
    file_n.close()
    
    #전체 작동 시간 표시
    print("실행 시간 : %s초" % (time() - start_time))
