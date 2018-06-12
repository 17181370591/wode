import requests,lxml,sys
from selenium import webdriver
from lxml import etree
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
se=requests.session()
url1='https://home.jd.com/'
url='https://passport.jd.com/new/login.aspx?'
r1=se.get(url,headers=headers)
co=se.cookies
co['TrackID']='14qbpI4wjVu13RNnXOTRQAIDddXqFpOj4KkgddMeH4WC7oET\
hLEqxochX3KcIh3lpPsPU8Jt3W08KqUCL8HVzOMDT1PdvwVHQVeSrZj7T964'
co['ceshi3.com']='201'
#co['TrackID']='1uUl2qYsoWONeHupu4MxtmK-0DqV1t-yPVKmGWSBJaLxLdgVE9UrRga7mxoClNKzQnTVMgzfltfLbKmSu6p2VbHcNf2hUegeMkUPaO5bh9t8'
#co['user-key']='7071317b-3ea4-4f8e-b126-77b1993000b2'
#co['UM_distinctid']='15ed8b3ed3d49-02cc4b4728936b-6b1b1279-1fa400-15ed8b3ed3f24a'
co['thor']='376E279740F11E64EADEE9AF350006C463B5D10B600F2\
AB8860237345064427F65E7DA16A45AEB6570AF64DD555159893B2D96\
7F3D1C2AEC8B88681CA4AD38281A0543F6DB8924E9E9D6465564E8AB12\
3A7F642FC0120E38549F3A07982FDCE869BA6C9A966CF4125E376FE5639\
BDC852027AB02FB343BC7A801F659AD9BC304B4D0CC4CB544659462F90A\
0496A9CF49B0386D145073595A6C21E66E99C67AA6'
r=se.get(url1)
with open(r'g://1.txt','w',encoding='utf-8') as f:
    f.write(r.text)
