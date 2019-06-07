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



def wordcloud_main(font_path, tag, imagefile):
    font_path = 'Maplestory_Bold.ttf'#글꼴 경로 설정
    wordcloud = WordCloud(font_path = font_path,
    width = 800,
    height = 600)#워드클라우드 사이즈
    open_input_file = []
    tag = open_input_file
    wordcloud.generate(tag)
    image = wordcloud.to_image()

    with imagefile:
        image.save('count', format='png', optimize=True)