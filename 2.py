import chardet,wordcloud as wc,numpy as np,re
from PIL import Image

f=open(r'C:\Users\Administrator\Desktop\1.txt','rb').read()[:20000]
ftype=chardet.detect(f)
print(ftype,len(f))
try:
    text=f.decode(encoding=ftype['encoding'])
except Exception as e:
    text=f.decode('gb18030')
text=re.sub(r'\s','',text)

fpath=r'simhei.ttf'

bg_pic=Image.open('1.jpg')
bg_pic_array=np.array(bg_pic)
pic= wc.WordCloud(max_words=77,
                 width=1000,height=100, mask=bg_pic_array,background_color='black',
    scale=1,font_path=fpath).generate(text)

pic.to_image().show()




