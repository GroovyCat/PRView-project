# 1. 웹크롤링에 필요한 모듈 호출
import requests # 특정 웹서버에 접근
from urllib.request import urlopen # 특정 웹서버에 접근
from bs4 import BeautifulSoup # 웹페이지 내용구조 해석

## 1. 1쪽 리뷰만 읽고 출력하기
# 2. 1번째 page 고객리뷰에접속 크롤링할 홈페이지 입력
url='http://member.auction.co.kr/Feedback/VIPFeedbackSecondList.aspx?sellerid=8949game&itemno=B556738715&categoryCode=15100100' #url 부분

# url을 읽어오는 용도 (둘중 하나 사용) 
page = requests.get(url).text 
#webpage = urlopen(url)

#테스트 url에 [원하는 값이 존재하나 테스트] (나중에 지울 것!)
print(requests.get(url)) #긍정 응답 확인용 [try문 사용해서 오류가 발생하면 사용자에게 알려주고 리턴]
#print(webpage)
#print(webpage.read())
#print(page)

# 3. 댓글 페이지 html 구조 긁어오기
source = BeautifulSoup(page,'html.parser',from_encoding='utf-8') # 한글이 있기때문에 encoding 해줌

# 4. 네티즌 댓글부분(태그 , {속성명: 속성값})   
reviews_title = source.findAll('div',{'class': 'coment-title'}) #제목 추출
reviews_Contents = source.findAll('p',{'class': 'coment'})      #내용 추출

# 5. 네티즌 별로 댓글 줄바꿔 출력하기
for review in reviews_title + reviews_Contents:
    print(review.get_text().strip())

print("\n end \n")  #종료 확인
    