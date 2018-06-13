#https://www.cnblogs.com/delav/p/7845539.html


import chardet,wordcloud as wc,numpy as np,re
from PIL import Image


f=open(r'C:\Users\Administrator\Desktop\1.txt','rb').read()[:20000]
ftype=chardet.detect(f)
print(ftype,len(f))
#ftype={'encoding': 'UTF-16', 'confidence': 1.0, 'language': ''}


try:
    text=f.decode(encoding=ftype['encoding'])
except Exception as e:
    text=f.decode('gb18030')
text=re.sub(r'\s','',text)              #用re去掉\t\n\s


fpath=r'simhei.ttf'

bg_pic=Image.open('1.jpg')
bg_pic_array=np.array(bg_pic)           #背景图需要array格式


#max_words表示热图里词的最大数量，默认200；font_path表示热图里词的字体，显示中文时必须设置否则汉字会变成方框；
#width，height表示画布属性，与mask（背景图片）冲突，scale表示mask的按比例缩放的值默认1
#background_color表示背景颜色，估计也与nask冲突
pic= wc.WordCloud(max_words=77,font_path=fpath
                  width=1000,height=100, mask=bg_pic_array,background_color='black',scale=1,).generate(text)

#pic.to_image()会生成图片，可以直接save
pic.to_image().show()




