import random,datetime
from collections import OrderedDict
import operator,os,re,time
random.seed(datetime.datetime.now())
pp='/11.txt'
def cj(pp):
    txt=open(os.getcwd()+pp,'r+',encoding='UTF-8').read()
    bd=['”','“','…','—','‘','’','\n']
    bd=r'”“…—‘’\n'
    txt=re.sub('[()（。. ，）"”阝“纟］：？…！—［扌‘’1234567890\n]','',txt)
#    print(len(txt))
    le=len(txt)
    di2={}
    for i in range(le-1):
        #li2.append((txt[i],txt[i+1]))
        if txt[i] not in di2:
            di2[txt[i]]={}
        if txt[i+1] not in di2[txt[i]]:
            di2[txt[i]][txt[i+1]]=1
        else:
            di2[txt[i]][txt[i+1]]=di2[txt[i]][txt[i+1]]+1
 #   for j in di2.items():
#        print(j)
    return di2    

def qz(dd):
    sum=0
    for i in dd.values():
        sum=sum+i
    jj=random.randint(1,sum)
    for z,j in dd.items():
        jj=jj-j
        if jj<=0:
            return z
def xss(a,b=7):
    ddc=cj(pp)
    txt=open(os.getcwd()+pp,'r+',encoding='UTF-8').read()
    jz=''
    cc=random.choice(txt)
    for i in range(a):
        jz=jz+cc
        cc=qz(ddc['%s' %cc])
        if not (i+1)%b:
            jz=jz+'\n'
    print(jz)
    
def xs(a,b=7):
    try:
        xss(a,b)    
    except KeyError as e:
        xss(20,5)
    
while True:
    try:
        xs(28)
        time.sleep(2)
    except KeyError as e:
        pass

