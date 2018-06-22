#关于rsa算法的原理，详见http://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html
#关于欧拉函数，详见https://blog.csdn.net/paxhujing/article/details/51353672

import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 

#生成一组随机数
rg=Random.new().read

#1024表示密匙是1024位，2**1024得到1个309位的10进制数，因为这个原因rsa.n正好109位？
rsa=RSA.generate(1024,rg)		#用随机数生成rsa（？）
grsa=rsa.publickey()			 

ss=rsa.exportKey()			 #生成私匙
gs=grsa.exportKey()			 #生成公钥

rsa=RSA.importKey(ss)			 #钥匙返回生成rsa（？）
grsa=RSA.importKey(gs)


#直接用公rsa对信息m加密，被加密的对象是bytes，base64编码后传输；
#传输的数据用base64解码后，用私匙解密，得到m
def ff(m):
    cis=PKCS1_v1_5.new(rsa)
    #cis=PKCS1_v1_5.new(RSA.importKey(ss))
    gcis=PKCS1_v1_5.new(grsa)
    #gcis=PKCS1_v1_5.new(grRSA.importKey(gs))
    e=gcis.encrypt(m.encode())
    d=base64.b64encode(e)
    print(d)
    c=base64.b64decode(d)
    print(cis.decrypt(c,'e'),type(c))


#信息j长度较大时无法一次加密，所以用le表示最大解密长度，分割j进行加密
#ll用来存储每一段的加密值，用b''.join合并ll生成一个长bytes返回
def f(j,le):
    ll=[]
    for i in range(0,len(j),le):
	ll.append(gcis.encrypt(j[i:i+le].encode()))
    return b''.join(ll)

#f生成的bytes较长时无法一次解密，所以用le表示最大解密长度，进行分割解密
#1024位密匙最大长度默认是128
def g(a,le=128):
    ll=b''  
    for i in range(0,len(a),le):
	ll+=cis.decrypt(a[i:i+le],'')
    return ll.decode()
  
ff('ggg')
