#coding=utf-8

from Crypto.Cipher import AES
import base64
from Crypto import Random

# padding算法
BS = AES.block_size # aes数据分组长度为128 bit

def pad(s):
    add=(BS - len(s)%BS) * chr(0)
    if add==16:add=0
    return (s + add).encode()

class aesdemo:
    def __init__(self, key,mode):
        self.key = key
        self.mode = mode
        
    def encrypt(self, plaintext):
        # 生成随机初始向量IV
        iv = Random.new().read(AES.block_size)
        print('encrypt_iv=',iv)
        cryptor = AES.new(self.key, self.mode, iv)
        
        ciphertext = cryptor.encrypt(pad(plaintext))
        #print(cryptor.decrypt)会报错，提示decrypt() cannot be called after encrypt()
        #似乎
        # 这里统一把加密后的字符串转化为16进制字符串
        return base64.b64encode(iv + ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)
        iv = ciphertext[0:AES.block_size]
        print('decrypt_iv=',iv)
        ciphertext = ciphertext[AES.block_size:len(ciphertext)]
        cryptor = AES.new(self.key, self.mode, iv)
        plaintext = cryptor.decrypt(ciphertext)
        return plaintext.decode().rstrip()

# 测试模块
if __name__ == '__main__':
    # 密钥长度可以为128 / 192 / 256比特，这里采用128比特
    # 指定加密模式为CBC
    demo = aesdemo(b'keyven__keyven__', AES.MODE_CBC)
    e = demo.encrypt('fuck you')
    d = demo.decrypt(e)
    print ("加密：", e)
    print ("解密：", d)
