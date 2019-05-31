'''
    텍스트 데이터를 기반으로 한 문장을 분석하여 명사를 추출하고 
    빈도수 별로 순위를 매겨 저장하기 위한 코드
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

def main():
    input_file = "input.txt" # 분석할 문장이 저장된 파일명
    result_file_ = "count.txt" # 분석된 명사들과 빈도를 저장하기 위한 파일명
    noun_count = 100 # noun_count 값 많큼의 명사를 추출

    open_input_file = open(input_file, 'r', -1, "utf-8") # 분석할 input.txt 파일 열기 
    text = open_input_file.read() # 해당 파일의 내용 읽기
    tags = get_tags(text, noun_count) # get_tags 함수 실행
    open_input_file.close() # 파일 닫기

    open_output_file = open(result_file, 'w', -1, "utf-8") # 결과로 쓰일 count.txt 열기
    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        open_output_file.write('{} {}\n'.format(noun, count)) # (명사 횟수)의 형태로 결과 파일에 저장
    open_output_file.close() # 파일 닫기
 
if __name__ == '__main__':
    main()
