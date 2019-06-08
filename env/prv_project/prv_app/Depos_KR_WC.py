from PIL import Image
import numpy as np

import matplotlib.pyplot as plt # 워드 클라우드 이미지 생성을 위한 import
from wordcloud import WordCloud
import random

def color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 100%%, %d%%)" % random.randint(60, 100)

dislike_mask = np.array(Image.open("dislike.png"))#싫어요 mask
font_path = './Maplestory_Bold.ttf' #폰트 path

wordcloud = WordCloud(
    font_path = font_path,
    width = 800,
    height = 800,
    background_color="white",#바탕색
    contour_width=1,#테두리 굵기
    contour_color='red',#테두리색
    mask = dislike_mask #마스크 설정
)

wordcloud = wordcloud.generate_from_frequencies(word_list)#워드클라우드 생성


fig = plt.figure(figsize=(10, 10))
plt.imshow(wordcloud.recolor(color_func=color_func, random_state=3),
           interpolation="bilinear")
#plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()#없애도 되는 코드 보여주기
fig.savefig('dislike_result.png')# 저장

