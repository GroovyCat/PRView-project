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
