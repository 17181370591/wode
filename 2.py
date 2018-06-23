from Crypto.Cipher import AES
import base64,random,math,json,fake_useragent as fu,requests
from Crypto import Random

BS = AES.block_size
c1={'rid': "R_SO_4_30953009", 'offset': "0", 'total': "true", 'limit': "20", 'csrf_token': "" }
c1=json.dumps(c1)
c2="010001"
c3='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
c4='0CoJUm6Qyw8W8jud'

def pad(s):
    if type(s)==type(''):
        add=(BS - len(s)%BS) 
        if add==16:add=0
        return (s + add* chr(0)).encode()
    return s

def a(a=16):
    b="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    c=""
    for d in range(0,a):
        e=random.random()*len(b)
        e=math.floor(e)
        c+=b[e]
    return c

def b(text,key,iv="0102030405060708"):
    print('111',pad(text))
    print('222',text.encode())
    cryptor = AES.new(pad(key), AES.MODE_CBC, pad(iv))
    m1=cryptor.encrypt(pad(text))
    m1=base64.b64encode(m1).decode()
    return  m1
    '''
    c=CryptoJS.enc.Utf8.parse
(b)
    d=CryptoJS.enc.Utf8.parse("0102030405060708")
    e=CryptoJS.enc.Utf8.parse(a)
    f=CryptoJS.AES.encrypt(e,c,
{iv:d,mode:CryptoJS.mode.CBC})
    return f.toString()
    '''
def get_p(d=c1,g=c4):
    m1=b(d,g)
    m1=b(m1,a())
    #m1=b(m1,"7T0gYR4aSnmDXz5S")
    print(m1)
    return m1
    
def c(a,b,c):
    pass
    #return setMaxDigits(131),d=new RSAKeyPair(b,"",c),e=encryptedString(d,a)

ep=get_p()
ek = 'a3b035e90d1ea623a41955b707c310b2e7a527f6a86d99cf483d9702c71038369ce5ffba782d5be5d9042fe91a076c92dc9c8c166ca775b38a247a0a73021506e12e5be60e572b75ab0e0030d3b724441f2671e08c5a487a89a5322d9ad6dd329ce8d13fe52f7eda67b04ba749305c7a4a10f7d6fa3b4b4edaf8e4efdda93f72'
print(ep)

ua=fu.UserAgent()
se=requests.session()
se.headers.update({'uset-agent':ua.random})
u3='http://music.163.com/#/song?id=30953009'
se.get(u3)
uu=r'http://music.163.com/weapi/v1/resource/comments/R_SO_4_30953009?csrf_token='
se.headers.update({'user-agent':u3})
datas={'params':ep,'encSecKey':ek}
print('datas=',datas)

r=se.post(uu,data=datas)
print(len(r.text))
se.close()
