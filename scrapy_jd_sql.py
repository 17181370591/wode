import pymysql,csv,os,time,re
from pymysql.err import IntegrityError
from 自动微信发信息 import main1,main2
def sele(table,*li):                     #查询  数据库
    cursele=con.cursor()
    sele=r'select {} from {}'.format(*li,table)
    cursele.execute(sele)
    c=cursele.fetchall()
    cursele.close()
    return c
def updat(table,*li):                       #添加url，价格和     #更新价格  #到数据库
    jdurl=[i[0] for i in sele(table,'jdurl')]
    jdid=[i[0] for i in sele(table,'jdid')]
    jd=sele(table,'*')
    curup=con.cursor()
    for i in li:
        try:
            if  i[0] in jdurl:
                s_up='update {} set xzjdjg="{}" where jdurl="{}"'.format(table,i[3],i[0])            
            elif i[0]!='@@@':
                s_up='insert into {}(jdurl,jdid,pcjg,xzjdjg,mj) values{}'.format(table,i)
            curup.execute(s_up)
        except IntegrityError as e:
            continue
    curup.execute(r'update {} set pcjg=xzjdjg where pcjg="";'.format(table))      #生成平常价格和从url生成id
    curup.execute(r'update  {} set jdid=replace(substring_index(jdurl,"/",-1),".html","")  where jdid="";'.format(table))  
    for i in li:
        
        if i[0]=='@@@':
            #print(chr(9)*8,i)
            sss=r'update {} set mj="{}" where locate("{}",jdurl)'.format(table,i[4],i[1])
            #print('*'*33)
            curup.execute(sss)
def setdata(filep):                     #读取1.csv的新数据生成固定顺序的list
    data=[]
    with open(filep,encoding="utf-8") as f:
        r=csv.DictReader(f)
        for i in r:
            if i['jdurl'] or i['jdid']:
                data.append((i['jdurl'].strip(),i["jdid"],i['pcjg'],i['xzjdjg'],i['mj'].strip()))
        return data
def js_jg(a,read):      #计算满减后的价格，只考虑打折，满减和送京豆
    re1=re.compile(r'(\d+)京豆')
    re2=re.compile(r'满(\d+)元.*?([\d.]+)元')    
    re3=re.compile(r'满(\d+)件.*?([\d.]+)折')
    try:
        try:
            s1r1=float(re1.search(read).group(1))*0.01       #减0.01*京豆
        except AttributeError as e:
            s1r1=0
        sr1=a-s1r1   
        try:
            s2=re2.findall(read)
            #print('s2',s2)
            if s2:
                if a<=max(float(tp[0]) for tp in s2):         #如果最大满a减b的a大于商品价格
                    sr2=min(1-float(ii[1])/float(ii[0]) for ii in s2)*a      #取最小折扣
                    #print('sr2=',sr2)
                else:sr2=a- max(float(tp[1]) for tp in s2)    #否则直接减最大的b
            else:sr2=a  
        except AttributeError as e:
            print(e)
            sr2=a
        #print('sr2=',sr2)    
        try:
            s3=re3.findall(read)
            if s3:
                sr3=min(0.1*float(ii[1]) for ii in s3)*a    #取最小折扣
                #print('sr3=',sr3)
            else:sr3=a    
        except AttributeError as e:
            print(e)
            sr3=a
        sr=min(sr1,sr2,sr3)
        #print('sr=',sr)
        return sr if sr>0 else a
    except Exception as e:
        print(e)
        return a                
##main1()
#time.sleep(60)
##os.chdir( r"C:\Users\Administrator\Desktop\scrapyproject\jd1") 
##os.system(r'scrapy crawl jd1  -o 1.csv --nolog')
con=pymysql.connect(user='root',passwd='',db='forpython',charset = 'utf8')



filep=r'C:\Users\Administrator\Desktop\scrapyproject\jd1\1.csv'
table='jd1'
tsele=sele(table,'*')               #读取数据库全部数据到tsele
lsele=[]
for i in tsele:
    l=list(i)
    l.append(round(js_jg(float(i[3]),i[4]),2))
    lsele.append(l)

c=updat(table,*setdata(filep))
fre=r'C:\Users\Administrator\Desktop\scrapyproject\jd1\jd1\spiders\fre.csv'
if os.path.exists(fre):
    os.remove(fre)
with open(fre,'w') as f:
    w=csv.writer(f)
    w.writerow(('jdurl','jdid','平常价格','京东现价','促销信息','满减价格'))
    w.writerows(lsele)



##with open(fre,"r",encoding="gb18030") as csvfile:          #发微信
##     #读取csv文件，返回的是迭代类型
##     read = csv.reader(csvfile)
##     for i in read:
##	     if(i) and i[0]!='jdurl':
##	          main2(r'{}原价{}现价{}优惠:{}&优惠价格:'.format(i[0],i[2],i[3],i[4],i[5]))
   
con.commit()
con.close()
    
