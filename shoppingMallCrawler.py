# 1. 웹크롤링에 필요한 모듈 호출
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains  #contril click in selenium
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석
from time import sleep  

driver = webdriver.Chrome('/Users/wkddn/Documents/crawling/ChromeDriver 74.0.3729.6/chromedriver')
#driver = webdriver.PhantomJS('/Users\/kddn/Documents/crawling/phantomjs-2.1.1-windows/bin/phantomjs') #판다스 사용할 경우 사용
driver.implicitly_wait(3)
 
# url에 접근한다.
driver.get('http://itempage3.auction.co.kr/DetailView.aspx?itemno=B362967210')
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

reviews_Contents=[] #저장할 리스트 변수
#페이지 수만큼 반복
for i in range(1,page_num+1):
    # 4. 네티즌 댓글부분(태그 , {속성명: 속성값})   
    page = driver.page_source
    source = BeautifulSoup(page,'html.parser',from_encoding='utf-8')
    revies_table = source.find('tbody') 
    #print(revies_table)

    #reviews_title = revies_table.findAll('strong') #제목 추출 수정필요
    reviews_Content = revies_table.findAll('a',{'id': 'ankContents'})      #내용 추출
   
    if(page_num>i): #마지막 페이지 전에 는 다음페이지 이동이 없음으로 
        driver.find_element_by_xpath("//a[@class='next']").click() #다음페이지 이동
    
    sleep(1)    #사이트에 부담을 줄이기위해 사용
   # print(i) #page 확인용
    for review in reviews_Content:
        reviews_Contents.append(review.get_text().strip().replace('\n','').replace('\t','').replace('\r',''))


print(reviews_Contents) #결과 출력

# 텍스트파일에 댓글 저장하기
file = open('shoppingMall.txt','w',encoding='utf-8')

for review in reviews_Contents:
    file.write(review+'\n')

file.close()

# end

#남은  부분
#사용자에게 입력 받을 부분 (사이트 or 영화명) , 긍부정 전체 분석 -> text
##영화와 사이트 class(매서드)로 구분 만들어줘야함