import requests,fake_useragent as fu


ua=fu.UserAgent()
se=requests.session()

u=r'https://www.zhihu.com/signup?next=%2F'
u1=r'https://www.zhihu.com/api/v3/oauth/sign_in'

d={"grant_type":'password',"username":'+8613311331133',\
   "password":'123456',"source":'com.zhihu.web',\
   "client_id":'c3cef7c66a1843f8b3a9e6a1e3160e20',\
   "timestamp":1528634801848,"captcha":'asdf',\
   "signature":'164b34ab62cb3e51f419e45afa2f698ff4dcd2d4',\
   "lang":'en',"ref_source":'homepage',"utm_source":None}
r=se.post(u1,data=d,headers={'user-agent':ua.random})
print(r.text)
