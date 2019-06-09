'''
    텍스트 데이터를 기반으로 한 문장을 분석하여 명사를 추출하고 
    빈도수 별로 순위를 매겨 저장하기 위한 모듈

    이 모듈이 같은 폴더, 하위 폴더에 있을 시
    from splitSen import get_tags(text: str, noun_count: int) 로 불러와서
    tags = get_tags(text: str, noun_count: int) 로 사용하면 됩니다. 

    이 모듈이 상위 폴더에 있을 시
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    을 추가해 절대경로 추가

    빈도 별 내림차순으로 정렬 된 리스트 반환
'''
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt # 워드 클라우드 이미지 생성을 위한 import
from wordcloud import WordCloud
import random
import numpy as np
from PIL import Image

def blue_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
    return "hsl(955, 100%%, %d%%)" % random.randint(40, 100)#"hsl(색, 다양성, )" % random.radint(밝기,)

def red_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
    return "hsl(0, 100%%, %d%%)" % random.randint(60, 100)

def get_tags_all_url(text, noun_count):
    spliter = Okt()
    nouns = spliter.nouns(text) # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns) # Counter 객체를 생성하고 참조변수 nouns할당
    return_list = {} # 명사와 빈도를 저장하기 위한 딕셔너리

    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도 수가
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    for n, c in count.most_common(noun_count):
        return_list[n] = c # {명사1 : 빈도, 명사2 : 빈도, 명사3 : 빈도 ...} 형식으로 딕셔너리 저장
    
    font_path = 'C:/Python_basic/env/prv_project/prv_app/Maplestory_Bold.ttf'#글꼴 경로 설정
    wordcloud = WordCloud(font_path = font_path, width = 300, height = 300)#워드클라우드 사이즈
    wordcloud = wordcloud.generate_from_frequencies(return_list)
    array = wordcloud.to_array()
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(array, interpolation="bilinear")
    plt.axis("off") # x, y 축의 scale을 안 보이도록 함
    #plt.show() # 생성한 워드 클라우드를 출력한다. 결과 확인용, 최종적으로는 없애도 되는 코드
    fig.savefig('C:/Python_basic/env/prv_project/prv_app/static/img_all/url_all.png') # 해당 이름으로 png 저장

def get_tags_pos_url(text, noun_count):
    spliter = Okt()
    nouns = spliter.nouns(text) # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns) # Counter 객체를 생성하고 참조변수 nouns할당
    return_list = {} # 명사와 빈도를 저장하기 위한 딕셔너리

    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도 수가
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    for n, c in count.most_common(noun_count):
        return_list[n] = c # {명사1 : 빈도, 명사2 : 빈도, 명사3 : 빈도 ...} 형식으로 딕셔너리 저장
    
    like_mask = np.array(Image.open("C:/Python_basic/env/prv_project/prv_app/static/img/like.png"))#좋아요 mask
    font_path = 'C:/Python_basic/env/prv_project/prv_app/Maplestory_Bold.ttf'#글꼴 경로 설정
   
    wordcloud = WordCloud(font_path = font_path, width = 800, height = 800,
        background_color="white",#
        contour_width=1,#테두리 굵기
        contour_color='steelblue',#테두리
        mask = like_mask #마스크 설정
    )
    wordcloud = wordcloud.generate_from_frequencies(return_list)#워드클라우드 생성

    array = wordcloud.to_array()
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud.recolor(color_func=color_func, random_state=3),interpolation="bilinear")
    plt.axis("off") # x, y 축의 scale을 안 보이도록 함
    #plt.show() # 생성한 워드 클라우드를 출력한다. 결과 확인용, 최종적으로는 없애도 되는 코드
    fig.savefig('C:/Python_basic/env/prv_project/prv_app/static/img_pos/url_pos.png') # 해당 이름으로 png 저장

def get_tags_neg_url(text, noun_count):
    spliter = Okt()
    nouns = spliter.nouns(text) # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns) # Counter 객체를 생성하고 참조변수 nouns할당
    return_list = {} # 명사와 빈도를 저장하기 위한 딕셔너리

    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도 수가
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    for n, c in count.most_common(noun_count):
        return_list[n] = c # {명사1 : 빈도, 명사2 : 빈도, 명사3 : 빈도 ...} 형식으로 딕셔너리 저장
   
    dislike_mask = np.array(Image.open("C:/Python_basic/env/prv_project/prv_app/static/img/dislike.png"))#싫어요 mask
    font_path = 'C:/Python_basic/env/prv_project/prv_app/Maplestory_Bold.ttf'#글꼴 경로 설정
   
    wordcloud = WordCloud(font_path = font_path, width = 800, height = 800,
    background_color="white",#바탕색
    contour_width=1,#테두리 굵기
    contour_color='red',#테두리색
    mask = dislike_mask #마스크 설정
    )
    wordcloud = wordcloud.generate_from_frequencies(return_list)#워드클라우드 생성
    array = wordcloud.to_array()
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud.recolor(color_func=color_func, random_state=3),interpolation="bilinear")
    plt.axis("off") # x, y 축의 scale을 안 보이도록 함
    #plt.show() # 생성한 워드 클라우드를 출력한다. 결과 확인용, 최종적으로는 없애도 되는 코드
    fig.savefig('C:/Python_basic/env/prv_project/prv_app/static/img_neg/url_neg.png') # 해당 이름으로 png 저장

def get_tags_all_movie(text, noun_count):
    spliter = Okt()
    nouns = spliter.nouns(text) # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns) # Counter 객체를 생성하고 참조변수 nouns할당
    return_list = {} # 명사와 빈도를 저장하기 위한 딕셔너리

    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도 수가
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    for n, c in count.most_common(noun_count):
        return_list[n] = c # {명사1 : 빈도, 명사2 : 빈도, 명사3 : 빈도 ...} 형식으로 딕셔너리 저장
    
    font_path = 'C:/Python_basic/env/prv_project/prv_app/Maplestory_Bold.ttf'#글꼴 경로 설정
    wordcloud = WordCloud(font_path = font_path, width = 300, height = 300)#워드클라우드 사이즈
    wordcloud = wordcloud.generate_from_frequencies(return_list)
    array = wordcloud.to_array()
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(array, interpolation="bilinear")
    plt.axis("off") # x, y 축의 scale을 안 보이도록 함
    #plt.show() # 생성한 워드 클라우드를 출력한다. 결과 확인용, 최종적으로는 없애도 되는 코드
    fig.savefig('C:/Python_basic/env/prv_project/prv_app/static/img_all/movie_all.png') # 해당 이름으로 png 저장

def get_tags_pos_movie(text, noun_count):
    spliter = Okt()
    nouns = spliter.nouns(text) # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns) # Counter 객체를 생성하고 참조변수 nouns할당
    return_list = {} # 명사와 빈도를 저장하기 위한 딕셔너리

    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도 수가
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    for n, c in count.most_common(noun_count):
        return_list[n] = c # {명사1 : 빈도, 명사2 : 빈도, 명사3 : 빈도 ...} 형식으로 딕셔너리 저장
    
    like_mask = np.array(Image.open("C:/Python_basic/env/prv_project/prv_app/static/img/like.png"))#좋아요 mask
    font_path = 'C:/Python_basic/env/prv_project/prv_app/Maplestory_Bold.ttf'#글꼴 경로 설정
   
    wordcloud = WordCloud(font_path = font_path, width = 800, height = 800,
        background_color="white",#
        contour_width=1,#테두리 굵기
        contour_color='steelblue',#테두리
        mask = like_mask #마스크 설정
    )
    wordcloud = wordcloud.generate_from_frequencies(return_list)#워드클라우드 생성

    array = wordcloud.to_array()
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud.recolor(color_func=blue_color_func, random_state=3),interpolation="bilinear")
    plt.axis("off") # x, y 축의 scale을 안 보이도록 함
    #plt.show() # 생성한 워드 클라우드를 출력한다. 결과 확인용, 최종적으로는 없애도 되는 코드
    fig.savefig('C:/Python_basic/env/prv_project/prv_app/static/img_pos/movie_pos.png') # 해당 이름으로 png 저장

def get_tags_neg_movie(text, noun_count):
    spliter = Okt()
    nouns = spliter.nouns(text) # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns) # Counter 객체를 생성하고 참조변수 nouns할당
    return_list = {} # 명사와 빈도를 저장하기 위한 딕셔너리

    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도 수가
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    for n, c in count.most_common(noun_count):
        return_list[n] = c # {명사1 : 빈도, 명사2 : 빈도, 명사3 : 빈도 ...} 형식으로 딕셔너리 저장
   
    dislike_mask = np.array(Image.open("C:/Python_basic/env/prv_project/prv_app/static/img/dislike.png"))#싫어요 mask
    font_path = 'C:/Python_basic/env/prv_project/prv_app/Maplestory_Bold.ttf'#글꼴 경로 설정
   
    wordcloud = WordCloud(font_path = font_path, width = 800, height = 800,
    background_color="white",#바탕색
    contour_width=1,#테두리 굵기
    contour_color='red',#테두리색
    mask = dislike_mask #마스크 설정
    )
    wordcloud = wordcloud.generate_from_frequencies(return_list)#워드클라우드 생성
    array = wordcloud.to_array()
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud.recolor(color_func=red_color_func, random_state=3),interpolation="bilinear")
    plt.axis("off") # x, y 축의 scale을 안 보이도록 함
    #plt.show() # 생성한 워드 클라우드를 출력한다. 결과 확인용, 최종적으로는 없애도 되는 코드
    fig.savefig('C:/Python_basic/env/prv_project/prv_app/static/img_neg/movie_neg.png') # 해당 이름으로 png 저장
