#地址：http://www.goubanjia.com/
#ip地址使用了display：none的数字来混淆
#port地址是通过class计算的，html文件上的port端口是假的

import requests,fake_useragent as fk
from lxml import etree
from functools import reduce

ua=fk.UserAgent()
se=requests.session()

u=r'http://www.goubanjia.com/'
r=se.get(u,headers={'user-agent':ua.random})
t=etree.HTML(r.text)
s=t.xpath(r'//td[@class="ip"]')


def f(v):       #计算传入classname，port
    s=['ABCDEFGHIZ'.index(i) for i in v]
    return int(reduce(lambda x,y:10*x+y,s)/8)

for s0 in s:
    z=s0.xpath('*[not(contains(@style,"none")) and not(contains(@class,"port"))]')
    zz=[i.xpath('string(.)') for i in z]
    print(*zz,sep='')
    p1=s0.xpath('*[contains(@class,"port")]')[0].attrib['class']
    #print('p1=',p1)
    port=f(p1.split(' ')[-1])
    print(':',port,'\n')

'''
解密后js如下
var _$ = ['.port', "each", "html", "indexOf", '*', "attr", 'class', "split", 
" ", "", "length", "push", 'ABCDEFGHIZ', "parseInt", "join", ''];

$(function() {
    $('.port').each(function() {
        var a = $(this).html();
        if (a.indexOf('*') != -0x1) {
            return
        }
        ;var b = $(this).attr('class');
        try {
            b = (b.split(" "))[0x1];
            var c = b.split("");
            var d = c.length;
            var f = [];
            for (var g = 0x0; g < d; g++) {
                f.push('ABCDEFGHIZ'.indexOf(c[g]))
            }
            ;$(this).html(window.parseInt(f.join('')) >> 0x3)
        } catch (e) {}
    })
})
'''
