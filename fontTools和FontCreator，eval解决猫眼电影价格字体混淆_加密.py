#http://maoyan.com/cinemas
#猫眼电影的价格使用了它自己定义的字体，源代码和审查工具里数字显示不正常
#猫眼电影的字体地址每次都会变，而且字体文件的编码和数字的顺序也会变，所以每次抓取价格需要在当前页面下载字体并分析
#这些数字的class=stonefont，这也是它使用的字体名字，搜索可以发现字体的地址就在html源代码里，后缀名是woff
#下载到本地后用fontTools分析，TTFont可以得到字体对象（？），getGlyphOrder可以得到编码顺序的对象（？），
#font['glyf'][i]（i是getGlyphOrder里的任意值）可以得到字符对象（？），英语差加上没有详细教程，这些对象的方法属性都不会，
#不过发现字符对象有个方法getMaxpValues()可以得到对于这个字体的不同数字的一一映射，所以用这个方法来识别数字
#字体还有yMax，xMin等属性，但这里不唯一所以不好用；字体分析依赖FontCreator


import requests,re,base64,fake_useragent as fu,re
from lxml import etree
from fontTools.ttLib import TTFont


ua=fu.UserAgent()
url=r'http://maoyan.com/cinemas'


r=requests.get(url,headers={'user-agent':ua.random}).text

re1=re.compile(r"url\('(//.*?woff)'\) format\('woff'\)")            #字体地址的re
font_u='https:{}'.format(re.search(re1,r).group(1))             
with open('qc.woff','wb') as f:
    f.write(requests.get(font_u).content)                       #保存字体到本地

    
#d是预先分析出0-9各自的getMaxpValues()的值，与nums一一对应
d=((32,2),(13, 1),(37, 1),(44, 1),(14, 2),(32, 1),(45, 2),(20, 1),(46, 3),(48, 2))
nums='0123456789'


nn=[]                               #nn用来保存字体中实际的数字的顺序
font=TTFont('qc.woff')

#li = font['cmap'].tables[0].ttFont.getGlyphOrder()
li = font.getGlyphOrder()               #很多教程用上面的写法，貌似这个也可以

#font.saveXML('li.xml')                 #可以在xml里查看字体的内容，不过看不懂

#生成ll使用了eval，eval('"\\u****"')可以得到\u****，直接拼接会报错或者生成\\u****
ll = [eval(r"'\u" + uni[3:] + "'") for uni in li[2:]]

for i in li[2:]:
    xp=font['glyf'][i].getMaxpValues()
    nn.append(nums[d.index(xp)])
print(nn)


#传入文本，返回用字体替换后的文本
#思路是：对于字体的每一个编码，如果该编码在文本a里出现，那么找到编码对应的数字x并替换
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

