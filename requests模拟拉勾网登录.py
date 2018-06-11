#https://passport.lagou.com/login/login.html
#fiddler里headers栏里貌似全部属于headers，这次的必须参数在headers里的 Miscellaneous 里
#方法是先get访问z，获取html里的两个参数，然后加入headers，在post访问ul

import requests,fake_useragent as fk,time,re
def login():
    ua=fk.UserAgent()
    se=requests.session()
    
    se.headers.update({'user-agent':ua.random})
    d={'isValidate':'true',
       'password':'d2e7c5f925057f7f49797c6ee0757ac6',
       'request_form_verifyCode':'',
       'submit':'',
       'username':'17010075310',
       }

    z='https://passport.lagou.com/login/login.json'
    ul='https://passport.lagou.com/login/login.html'    
    r2=se.get(ul)
    re1=re.compile(r"window.X_Anti_Forge_Token = \'(.*?)';",re.S)
    re2=re.compile(r"window.X_Anti_Forge_Code = \'(.*?)';",re.S)
    h1=re.search(re1,r2.text).group(1)
    h2=re.search(re2,r2.text).group(1)
    se.headers.update({'X-Anit-Forge-Token' : h1})
    se.headers.update({'X-Anit-Forge-Code' : h2})
    se.headers.update({'Referer':ul})
    print('se.headers=',se.headers)
    response = se.post(z, data=d)
    print(response.content.decode('utf-8'))
          
if __name__ == "__main__":
    login()
