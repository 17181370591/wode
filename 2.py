#http://maoyan.com/cinemas

import requests,re,base64,fake_useragent as fu,re
from lxml import etree
from fontTools.ttLib import TTFont


ua=fu.UserAgent()
url=r'http://maoyan.com/cinemas'


r=requests.get(url,headers={'user-agent':ua.random}).text
re1=re.compile(r"url\('(//.*?woff)'\) format\('woff'\)")
font_u='https:{}'.format(re.search(re1,r).group(1))
with open('qc.woff','wb') as f:
    f.write(requests.get(font_u).content)

d=((32,2),(13, 1),(37, 1),(44, 1),(14, 2),(32, 1),(45, 2)
      ,(20, 1),(46, 3),(48, 2))
nums='0123456789'
nn=[]
font=TTFont('qc.woff')
#li = font['cmap'].tables[0].ttFont.getGlyphOrder()
li = font.getGlyphOrder()  
#font.saveXML('li.xml')
#getMaxpValues
ll = [eval(r"'\u" + uni[3:] + "'") for uni in li[2:]]
for i in li[2:]:
    xp=font['glyf'][i].getMaxpValues()
    nn.append(nums[d.index(xp)])
print(nn)

def change(a):
    for i in ll:
        if i in a:
            x=nn[ll.index(i)]
            a=a.replace(i,x)
    return a



t=etree.HTML(r)
s=t.xpath('//span[@class="stonefont"]')

for i in s:
    print(change(i.xpath('string(.)')))

