from PIL import Image
import numpy as np

import matplotlib.pyplot as plt # 워드 클라우드 이미지 생성을 위한 import
from wordcloud import WordCloud
import random

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 100%%, %d%%)" % random.randint(60, 100)
