import pymysql,csv,re
import numpy as np,pandas as pd
r1=re.compile(r'(\d+)g',re.I)
con=pymysql.connect(host='127.0.0.1',port=3306,user='root',db='forpython',charset='utf8')
cur=con.cursor()
u=r'https://item.jd.com/{}.html'
s1=r'select * from jd_price where beizhu="瓜子"'
cur.execute(s1)
s=cur.fetchall()
p=pd.DataFrame(np.array(s))
z=p.ix[:,7]
def f(x):
    try:
        return float(re.search(r'(\d+)g',x).group(1))/500
    except Exception as e:
        return -1
zz=z.map(f)
p['price_jin']=p.ix[:,6].map(float)/zz
pp=p[p['price_jin']>0]
pp[1]=pp[1].map(lambda x:u.format(x))
pp.sort_values('price_jin',inplace=True)
ppp=pp.ix[:,[1,5,6,7,8,'price_jin']]
ppp.columns=['num','url','促销','活动价','name','每斤价格']
ppp.index=range(1,len(ppp)+1)
ppp.to_csv('1.csv')
cur.close()
con.close()
##with open('1.csv','w',newline='') as f:
##    c=csv.writer(f)
##    c.writerow(('num','jd_id','check_time','price_now','price_av','act','price_act','jd_name','check_time','beizhu'))
##    for i in p:
##        
##        c.writerow(i)
