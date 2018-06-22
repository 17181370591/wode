#windows中使用Python进行AES加密解密-加密解密功能实现
#原地址：https://blog.csdn.net/u013578500/article/details/77905924
#下面代码的a2b_hex和b2a_hex可以写成base64.b64encode和base64.b64decode
#本文代码全部没有测试，仅做检索用

'''
1.预处理
AES有三种密钥长度16(*AES-128*), 24 (*AES-192*), 和 32 (*AES-256*)，在对字符进行加密时，
密码和明文长度必须为16,24,或32。因此要对密码和明文进行预处理，确保密码长度为16,24或32，
明文长度为16,24或32的整数倍，这里以16(*AES-128*)为例，代码如下：
'''
# 补全字符  
def align(str, isKey=False):  
    # 如果接受的字符串是密码，需要确保其长度为16  
    if isKey:  
        if len(str) > 16:  
            return str[0:16]  
        else:  
            return align(str)  
    # 如果接受的字符串是明文或长度不足的密码，则确保其长度为16的整数倍  
    else:  
        zerocount = 16-len(str) % 16  
        for i in range(0, zerocount):  
            str = str + '\0'  
        return str  
    
    
    
'''  
2.加密
要调用PyCrypto的AES加密模块，首先导入AES的包，另外为了确保编码的统一，我选择将密文保存为16进制，
因此还需要从binascii中导入b2a_hex和a2b_hex。
这里使用的是ECB的加密模式，AES共有五种加密模式（ECB，CBC，PCBC，CFB，OFB，CTR）.
这里加密函数的流程是：预处理密码和明文->初始化AES->加密->转码->输出结果，代码如下：
'''

from Crypto.Cipher import AES
from binascii import b2a_hex
from binascii import a2b_hex
# ECB模式加密  
def encrypt_ECB(str, key):  
    # 补全字符串  
    str = align(str)  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_ECB)  
    # 加密  
    cipher = AESCipher.encrypt(str)  
    return b2a_hex(cipher)  




#3.解密
#这里解密的流程是：预处理密码->初始化AES->转码->解密->输出结果，代码如下：
# ECB模式解密  
def decrypt_ECB(str, key):  
    # 补全字符串  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_ECB)  
    # 解密  
    paint = AESCipher.decrypt(a2b_hex(str))  
    # 去除/0    
    paint = paint.rstrip('\0')    
    return paint  



''' 
4.AES加密模式——CBC
上面的示例代码使用的是ECB模式进行加密解密，这种模式比较简单，并且安全性相对较差，
关于这一点，wiki上有张图我觉得十分形象。
（https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Initialization_vector_.28IV.29） 
大部分场景下，我们会使用CBC模式来进行AES加密，和ECB相比，CBC引入了初始向量IV（Initialization vector），
每一次加密都使用随机产生的初始向量可以大大提高密文的安全性（这里的示例代码使用固定的IV），代码如下。
'''
# CBC模式加密  
def encrypt_CFB(str, key):  
    # 补全字符串，虽然明文长度没有限制，但是密码仍然需要16位  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_CBC, '1234567890123456')  
    # 加密  
    cipher = AESCipher.encrypt(str)  
    return b2a_hex(cipher)  
  
  
# CBC模式解密  
def decrypt_CFB(str, key):  
    # 补全字符串  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_CBC, '1234567890123456')  
    # 解密  
    paint = AESCipher.decrypt(a2b_hex(str))  
    # 去除/0  
    paint = paint.rstrip('\0')  
    return paint  



#5. AES加密模式——CFB
#除了CBC模式，这里再介绍一种加密模式——CFB模式，这个模式下明文长度可以不为16的整数倍，代码如下：
# CFB模式加密  
def encrypt_CFB(str, key):  
    # 补全字符串，虽然明文长度没有限制，但是密码仍然需要16位  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_CFB, '1234567890123456')  
    # 加密  
    cipher = AESCipher.encrypt(str)  
    return b2a_hex(cipher)  
  
  
# CFB模式解密  
def decrypt_CFB(str, key):  
    # 补全字符串  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_CFB, '1234567890123456')  
    # 解密  
    paint = AESCipher.decrypt(a2b_hex(str))  
    # 去除/0  
    paint = paint.rstrip('\0')  
    return paint  


#6.完整的实例代码如下

from Crypto.Cipher import AES  
from binascii import b2a_hex  
from binascii import a2b_hex  
  
# 补全字符  
def align(str, isKey=False):  
    # 如果是密码，需要确保其长度为16  
    if isKey:  
        if len(str) > 16:  
            return str[0:16]  
        else:  
            return align(str)  
    # 如果是被加密字符串或长度不足的密码，则确保其长度为16的整数倍  
    else:  
        zerocount = 16-len(str) % 16  
        for i in range(0, zerocount):  
            str = str + '\0'  
        return str   
 
  
# ECB模式加密  
def encrypt_ECB(str, key):  
    # 补全字符串  
    str = align(str)  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_ECB)  
    # 加密  
    cipher = AESCipher.encrypt(str)  
    return b2a_hex(cipher)   
  
  
# ECB模式解密  
def decrypt_ECB(str, key):  
    # 补全字符串  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_ECB)  
    # 解密  
    paint = AESCipher.decrypt(a2b_hex(str))  
    # 去除/0  
    paint = paint.rstrip('\0')  
    return paint  
  
  
  
  
# CBC模式加密  
def encrypt_CBC(str, key):  
    # 补全字符串  
    str = align(str)  
    key = align(key, True)  
    # 初始化AES，引入初始向量  
    AESCipher = AES.new(key, AES.MODE_CBC, '1234567890123456')  
    # 加密  
    cipher = AESCipher.encrypt(str)  
    return b2a_hex(cipher)  
  
  
  
  
# CBC模式解密  
def decrypt_CBC(str, key):  
    # 补全字符串  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_CBC, '1234567890123456')  
    # 解密  
    paint = AESCipher.decrypt(a2b_hex(str))  
    # 去除/0  
    paint = paint.rstrip('\0')  
    return paint  
  
  
  
  
# CFB模式加密  
def encrypt_CFB(str, key):  
    # 补全字符串，虽然明文长度没有限制，但是密码仍然需要16位  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_CFB, '1234567890123456')  
    # 加密  
    cipher = AESCipher.encrypt(str)  
    return b2a_hex(cipher)  
  
  
  
  
# CFB模式解密  
def decrypt_CFB(str, key):  
    # 补全字符串  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_CFB, '1234567890123456')  
    # 解密  
    paint = AESCipher.decrypt(a2b_hex(str))  
    # 去除/0  
    paint = paint.rstrip('\0')  
    return paint  
  
  
  
  
# OFB模式加密  
def encrypt_OFB(str, key):  
    # 补全字符串  
    str = align(str)  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_OFB, '1234567890123456')  
    # 加密  
    cipher = AESCipher.encrypt(str)  
    return b2a_hex(cipher)  
  
  
  
  
# OFB模式解密  
def decrypt_OFB(str, key):  
    # 补全字符串  
    key = align(key, True)  
    # 初始化AES  
    AESCipher = AES.new(key, AES.MODE_OFB, '1234567890123456')  
    # 解密  
    paint = AESCipher.decrypt(a2b_hex(str))  
    # 去除/0  
    paint = paint.rstrip('\0')  
    return paint  
  
  
# 先设置一段明文和密码  
Text = 'Suprise！！****** *****r!'  
key = 'mor'  
  
  
# ECB模式加密  
ciphertext = encrypt_ECB(Text, key)  
print ("ECB模式密文：" + ciphertext)  
# ECB模式解密  
plaintext = decrypt_ECB(ciphertext, key)  
print ("ECB模式明文：" + plaintext)  
  
  
# CBC模式加密  
ciphertext = encrypt_CBC(Text, key)  
print ("CBC模式密文：" + ciphertext)  
# CBC模式解密  
plaintext = decrypt_CBC(ciphertext, key)  
print ("CBC模式明文：" + plaintext)  
  
  
# CFB模式加密  
ciphertext = encrypt_CFB(Text, key)  
print ("CFB模式密文：" + ciphertext)  
# CFB模式解密  
plaintext = decrypt_CFB(ciphertext, key)  
print ("CFB模式明文：" + plaintext)  
  
  
# OFB模式加密  
ciphertext = encrypt_OFB(Text, key)  
print ("OFB模式密文：" + ciphertext)  
# OFB模式解密  
plaintext = decrypt_OFB(ciphertext, key)  
print ("OFB模式明文：" + plaintext)  
