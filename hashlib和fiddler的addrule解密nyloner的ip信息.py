#https://zhuanlan.zhihu.com/p/30461975
#https://www.nyloner.cn/proxy

import base64

#抓包发现该网站的ip信息由proxy.js加载，下载js后发现由get_proxy_ip生成，使用execjs各种找不到对象，
#在下载的js文件中get_proxy_ip里加入console语句，然后用fiddler的add rule，
#将原js替换成本地的js，可在控制台查看各参数，d也是这么获取的，
#该函数又调用了同js的decode_str，这个函数用python写代码如下ds函数

#hashlib函数的decodestring和encodestring已被替换成decodebytes和encodebytes，
#参数都是类bytes格式，需要注意a和a.encode()的长度一般不一样（全是字母和数字时一样），


d=r'OUofBg0iSxcdLyZYLDEnASErLx0/LTAfJi0vQg8uXQMnDx0JMAYmGSgmCQ0hKzcRPwQ4CyI6JEQgLQ9ZIw8jBzUvLgcEKi8QIwYvDD06KBkiBDQLIhM5WyIPN140BSVXKTEsTiUBLBMRACgFIAckGyMtLRgjMTMHNS8uBwE1Ag02PCdTOy0wFSIqIEYiLS1dIjE7GTAoKhkqGDtKIwUnVTsHDgsmAwkFJxMDCCcPGV41BiZeKBtaSCMsWh08LTNVIy0nRScXLhkNCyMHNgUuBygmLw4hOy8MPi04BQspCQY0KiVZJyY7FzQoKlopJi9LIDsnEjsqPBsgBDBBIRMlXycMBQkwAQMZLBgBHiUFBVU+BDBcIgdRQyEqWBYgIScHHz8YCQALJA4OXCRVOwQWCyYENAojEyFaJwwFCTACPR4HJTsQIwYvDD8EOBQgLVUFIBBcFiMmMxY0KABfKBgBACEWJxY7LTMcDC0sRCc6JRcjMSsbNzgIGygYI0ggBStQPS0zVSMtJ0UnFy4ZDQsjBzYFLgcoCCsAIywnFjstM1wOOVQeJxMDCCcPOxk0OAgaKDY3DSEFLwI/OjhaITosRCMTKQYiJjMHGDQuByobLxAhOy8fPgQaXCMEIAsjOlgXIx8ZBx8/GAkACyQODlwkVTsEFgsmBAIFIT0tBiImMwcdKwMaPyEnTyUsJxw/KjxYIzokQCItJRgnITcZNgY6FyoYJw4lBhkCOwMVGyYEChUnEykYIxxGFzcoJhsoGCtMIAUnVT8HM1UjLSdFJxcuGQ0LIwc2BS4HKjYvTSEsJxY7LTNcDjlUHicTAwgnDzsZNDgIGig2Nw0hBS8CPzo4WiE6LEQjEy0GIiYzBxg0LgcqGy8QITsvHz4EMFwgLVELIwMlGiMxP18wAl8dLDodEA8oVxwWLTBaJi0sRiE9NV0nDAUJMAI9HgclOxAjBi8MPwQ4FCAtVQUgEFwWIyYzFjQoAF8oGAEBIzwnFjstMxwMLSxEJzolFyMhNxs0BiJcKRg7AyAFJ1Q/LTNVIy0nRScXLhkNCyMHNgUuByo2CUsiBicWOy0zXA45VB4nEwMIJw87GTQ4CBooNjcNIQUvAj86OFohOixEIy0LBiImMwcYNC4HKhsvECE7Lx0+BDAWIQdRQiAAWBYgMTcHHz8YCQALJA4OXCRVOwQWCyYEKAojEwsGIiYzBx0rAxo/ISdPJSwnHD8qPFgjOiRAIi0lGCchNxk2BjoXKhgrTSUGGQI7AxUbJgQKFScTKRgjNkYUNxVbXSohWgEhBTsMFD0OCwoXLwUMSiZfJw8dCTAGCBkqNi8QICwvDBYpFRg1PSxEJzolFiMhN1o1OC5cKSYnDiUrKxI9BCwVIAQgRicQGwgnCB4ZMAYACSwYKwEhLFodPAQoGSI6AgoiEyldICY4VzUvLVksHCwPDwE/DD0HOAUgKgJAIBAlHCcmOF4YO14CLBgBHiUFJxI/Oh4YIio8BiMTLQgjMTNYNzgmWCgmDRAgLC8MEzY4BSAHJBsjLS0XIg87FDcFWxQqMVoAIjs/DBQ9DgsKFy8FDEomXycPHQkwBggZKCYvECAsLwwWKRUYNT0sRCc6JRYjITdaNTguXCkmJw4lKysSPQQsFSAEIEEnEBsIJwgeGTAGAAksGCsBIRZaHD8qOBkhOjwHIy0hBgg2BQkcFSUZB0EkSSUFAQI7BDQUIgQCGyI6LQYKIh4aIz8mWCwxJwAhKytRPjo4XiM6LAUnPSkYIQ8nFzYGKl0sGxkeJQICEjsEFgsmBCAKIDpYFiMxJxs2ODobKCYJTSUBXhY7JgoFDClcCwo6JVknJjtaNigIWiwbGR4lATwVEDksBSAHJBsjEy0XISZCGTcFXxcoMS8BISsBVD8EFhQhBywBJzomHw0mO1gwLyYWKAgFDCEFJ1U+BDBcIwQsQCcXXQs='


def ds(d):
    le1=len(d)
    d=base64.decodebytes(d.encode())
    print(le1==len(d))
    print(d,type(d))
    key = b'nyloner'
    code = ''
    for i in range(len(d)):
        l=i%len(key)
        code+=chr(d[i]^key[l])
    print(code,type(code))
    s1=base64.decodebytes(code.encode())
    print(s1,type(s1))
    s2=s1.decode()
    print(s2.type(s2))
    return s2

s1=ds(d)    
    
