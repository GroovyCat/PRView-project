from PIL import Image
import numpy as np
from . import splitSent
import matplotlib.pyplot as plt # 워드 클라우드 이미지 생성을 위한 import
from wordcloud import WordCloud
import random

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(955, 100%%, %d%%)" % random.randint(40, 100)#"hsl(색, 다양성, )" % random.radint(밝기,)
