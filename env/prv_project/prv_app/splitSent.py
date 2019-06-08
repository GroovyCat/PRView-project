'''
    명사 분석 및 워드 클라우드 이미지 생성을 위한 코드
    
    get_tags(text :str, noun_count :int) 형태로 호출하면 됩니다.
    폰트 파일은 해당 코드와 같은 폴더 내에 있으면 됩니다.
    생성된 워드 클라우드 이미지도 같은 폴더에 저장됩니다.
'''
from konlpy.tag import Okt # 명사 빈도 추출을 위한 라이브러리
from collections import Counter
# import matplotlib.pyplot as plt # 워드 클라우드 이미지 생성을 위한 import
# from wordcloud import WordCloud

def get_tags(text, noun_count):
    spliter = Okt()
    nouns = spliter.nouns(text) # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns) # Counter 객체를 생성하고 참조변수 nouns할당
    return_list = [] # 명사, 빈도 딕셔너리를 저장할 리스트

    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도 수가
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    for n, c in count.most_common(noun_count):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    
    return return_list

'''
def get_tags(text, noun_count):
    spliter = Okt()
    nouns = spliter.nouns(text) # nouns 함수를 통해서 text에서 명사만 분리/추출
    count = Counter(nouns) # Counter 객체를 생성하고 참조변수 nouns할당
    word_list = {} # 명사와 빈도를 저장하기 위한 딕셔너리

    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도 수가
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    for n, c in count.most_common(noun_count):
        word_list[n] = c # {명사1 : 빈도, 명사2 : 빈도, 명사3 : 빈도 ...} 형식으로 딕셔너리 저장

    font_path = './Maplestory_Bold.ttf' # 한글 인식을 위한 폰트 파일. 같은 폴더 안에 있어야 함
    wordcloud = WordCloud(font_path = font_path, width = 800, height = 800) # 워드 클라우드의 폰트와 가로세로 크기 지정
    wordcloud = wordcloud.generate_from_frequencies(word_list) # 딕셔너리의 명사를 그 빈도에 비례하여 글자 크기를 키워주는 워드클라우드
    
    array = wordcloud.to_array()
    print(type(array)) # numpy.ndarray
    print(array.shape) # (800, 800, 3)
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(array, interpolation="bilinear")
    plt.axis("off") # x, y 축의 scale을 안 보이도록 함
    plt.show() # 생성한 워드 클라우드를 출력한다. 결과 확인용, 최종적으로는 없애도 되는 코드
    fig.savefig('result.png') # 해당 이름으로 png 저장
'''
