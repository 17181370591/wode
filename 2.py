#关于rsa算法的原理，详见http://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html
#关于欧拉函数，详见https://blog.csdn.net/paxhujing/article/details/51353672

import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 

rg=Random.new().read

#1024表示密匙是1024位，2**1024得到1个309位的10进制数，因为这个原因rsa.n正好109位？
rsa=RSA.generate(1024,rg)
grsa=rsa.publickey()

ss=rsa.exportKey()
gs=grsa.exportKey()

rsa=RSA.importKey(ss)
grsa=RSA.importKey(gs)

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

def f(j,le):
    ll=[]
    for i in range(0,len(j),le):
	ll.append(gcis.encrypt(j[i:i+le].encode()))
    return b''.join(ll)

def g(a,le=128):
    ll=b''  
    for i in range(0,len(a),le):
	ll+=cis.decrypt(a[i:i+le],'')
    return ll.decode()
  
ff('ggg')
