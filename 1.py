from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64


#===============================================
# 伪随机数生成器

random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

# master的秘钥对的生成
sp = rsa.exportKey()
gp=rsa.publickey().exportKey()
with open('sp.pem','wb') as f:
    f.write(sp)
with open('gp.pem','wb') as f:
    f.write(gp)


#===============================================


message = 'hello ghost, this is a plian text'
with open('gp.pem') as f:
    key1=f.read()
    rsakey1=RSA.importKey(key1)     #rsakey1==rsa.publickey()
    cipher1=Cipher_pkcs1_v1_5.new(rsakey1)
    cipher_text=base64.b64encode(cipher1.encrypt(
        message.encode(encoding="utf-8")))
    print(cipher_text)

with open('sp.pem') as f:
    key2 = f.read()
    rsakey2 = RSA.importKey(key2)  # 导入读取到的私钥,rsakey2==rsa
    cipher2 = Cipher_pkcs1_v1_5.new(rsakey2)  # 生成对象
    text2 = cipher2.decrypt(base64.b64decode(cipher_text), "ERROR")  # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
    print(text2)
