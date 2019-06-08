from PIL import Image
import numpy as np

import matplotlib.pyplot as plt # 워드 클라우드 이미지 생성을 위한 import
from wordcloud import WordCloud
import random

def color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(955, 100%%, %d%%)" % random.randint(40, 100)#"hsl(색, 다양성, )" % random.radint(밝기,)


like_mask = np.array(Image.open("like.png"))#좋아요 mask
font_path = './Maplestory_Bold.ttf' #폰트 path

wordcloud = WordCloud(
    font_path = font_path,
    width = 800,
    height = 800,
    background_color="white",#
    contour_width=1,#테두리 굵기
    contour_color='steelblue',#테두리
    mask = like_mask #마스크 설정
)

wordcloud = wordcloud.generate_from_frequencies(word_list)#워드클라우드 생성

fig = plt.figure(figsize=(10, 10))
plt.imshow(wordcloud.recolor(color_func=color_func, random_state=3),
           interpolation="bilinear")
#plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("
plt.show()#없애도 되는 코드 보여주기
fig.savefig('like_result.png')# 저장
