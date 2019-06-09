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
     3. 해당 크롤링 하는 기능은 상품 리뷰 크롤링 함수와 영화 리뷰 크롤링 함수 총 2개로 나뉘어져 있습니다.
     4. 해당 크롤링 하는 것은 전체 리뷰 데이터 크롤링, 긍정 단어 데이터 크롤링, 부정 단어 데이터 크롤링 총 3개의 데이터 파일로 추출된다.
   - 자연어 처리
     1. 해당 크롤링 된 데이터 파일(.txt. 파일)을 명사를 기준으로 해 split한후 단어 데이터를 추출한다.
     2. 해당 단어 데이터는 딕셔너리 형태로 반환된다.
     3. 단어 데이터는 해당 단어의 빈도수를 포함한다.
     4. 라이브러리는 konlpy를 가져와 사용했다.(형태소 분석)
     5. 해당 자연어 처리된 것은 전체 리뷰 데이터, 긍정 단어 데이터, 부정 단어 데이터로 나뉜다.
   - 데이터 시각화
     1. 데이터 시각화 도구는 wordcloud 라이브러리를 이용해 데이터 시각화를 표현한다.
     2. 해당 자연어 처리된 딕셔너리 형태를 받아와 시각화 이미지를 추출한다.
     3. 각 해당 이미지는 폴더에 저장한다.
     4. 각 주제별로 마스킹한 이미지로 워드 클라우드가 생성된다.
   - front-end
     1. html과 css을 사용해 웹을 개발하였다.
     2. bootstrab를 활용해 css와 grid를 설정하였다.
     3. 각 html에서 python 프로그램이 동작하도록 django Templete를 이용했다.
   - back-end
     1. django상에서 백엔드 처리를 하였다.
     2. SQLite3를 써서 입력 받은 text 데이터를 저장하는 상품 URL DB와 영화명 DB를 모델링하였다.
     3. 각 주제별 이미지가 해당 폴더 경로에 있으면 관련 html로 이동하도록 개발하였다.
     4. 만약 해당 주제별 크롤링 데이터 파일의 내용이 없는 경우는 전 과정에서 생성된 이미지를 삭제하도록 하고 에러 이미지를 호출한다.
     5. 입력 text 데이터는 해당 html로 이동할때 문자열의 길이값을 가지고 와 해당 문자열 길이가 20보다 큰 경우에 상품 URL 관련 html로
        이동하도록 만들었다. 반대로 작은 경우는 영화명 관련 html로 이동한다.
     6. 문자열의 길이값을 가지고 오는 이유는 상품 URL 문자열의 길이가 영화명 문자열의 길이보다 크기 때문에 비교하기 위해서 불러온다.
3. Development Results

   현재 구현하고자 하는 기능은 다 구현한 상태이며, 원래 계획했던 전에 생성됐던 이미지를 다시 보여주는 기능은 시간의 문제가 있어 미 구현상태이다.
   추후에 개발을 더 진행한다면 구현할 예정이다.
