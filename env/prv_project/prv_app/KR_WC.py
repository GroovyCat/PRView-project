import sys
import textwrap
import io
import re
import argparse
from PIL import Image

#from krwordrank.word import KRWordRank
from konlpy.tag import Mecab
from collections import Counter
from wordcloud import WordCloud



def main(font_path, text, imagefile):
    font_path = 'Maplestory_Bold.ttf'#글꼴 경로 설정
    wordcloud = WordCloud(font_path = font_path,
    width = 800,
    height = 600)#워드클라우드 사이즈
    open_input_file = open('count.txt', 'r', -1, "utf-8")
    text = open_input_file.read() # 해당 파일의 내용 읽기
    wordcloud.generate(text)
    image = wordcloud.to_image()

    with imagefile:
        image.save('count', format='png', optimize=True)
