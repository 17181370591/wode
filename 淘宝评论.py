#encoding=utf-8
#抓取淘宝评论


import requests,lxml,json,re,pandas,time

u='https://rate.taobao.com/feedRateList.htm?auctionNumId=559466668836&\
userNumId=1074549940&currentPageNum={}&pageSize=20'
pa=251
for i in range(1,pa):
    time.sleep(1)
    l=[]
    se=requests.session()
    u1=u.format(i)
    r=se.get(u1)
    r1=re.sub("u'","\"",r.text)
    r1=re.sub("'","\"",r1)
    
  
    #重要，json格式有时无法loads，原因是源文件并不是一个字典，
    #需要删除字典外边的部分
    r1=r1[3:-2]
    
    r2=json.loads(r1)
    r3=r2['comments']
    for j in range(len(r3)):
        try:
            nick=r3[j]['user']['nick']
        except Exception:
            nick=''
        try:
            num=r3[j]['buyAmount']
        except Exception:
            num=''
        try:
            date=r3[j]['date']
            #print(date)
        except Exception:
            date=''        
        try:
            content=r3[j]['content']
        except Exception:
            content=''
        try:
            sku=r3[j]['auction']['sku']
        except Exception:
            sku=''
        try:
            amount=r3[j]['bidPriceMoney']['amount']
        except Exception:
            amount=''             
        l.append((nick,date,content,sku,amount,num))
    print(i,len(l))            
    l=pandas.DataFrame(l)

    #注意to_csv的参数，分别是encoding（utf-8的写法），mode='a'表示添加在尾部，
    #header=None表示不要标题
    gg='utf_8_sig'
    gg='gb18030'    
    l.to_csv('2.csv',encoding=gg,mode='a',header=None)
    
    if len(l)<20:
        break
    
