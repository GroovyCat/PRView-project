# PReView-project

주제 : 상품 리뷰 데이터 & 영화 리뷰 데이터를 통한 데이터 시각화

1. Project Start : the first semester of the third grade

2. Project Personnel : 4 people

3. Project Member : 채윤재(팀장) 지하린 박문영 장우성

# 개발 내용

1. Development Environment : VS Code, Python, Django 

2. Development method 

   해당 프로그램은 웹사이트에서 상품 리뷰 데이터 혹은 영화 리뷰 데이터를 크롤링 하고 자연어 처리를 통해 단어 빈도수를 추출한 후 워드 클라우드 이미지로 데이터 시각화를 하는 웹사이트입니다. 상품 리뷰 데이터는 옥션 사이트를 기준으로 했으며, 영화 리뷰 데이터는 네이버 영화를 기준으로 잡았다. 각 해당 기능에 대해서 설명하도록 한다.
   - 크롤링 기능
     1. 크롤링하는 것은 selenium이라는 크롤링 라이브러리를 사용해 동적으로 크롤링으로 할 수 있도록 하였다.
     2. 현 웹사이트에서 상품 링크 주소나 영화명을 입력시 search 버튼을 누르면 webdriver를 통해 크롤링 되는 것을 확인할 수 있다.
     3. 
