import csv,time
import numpy as np,pandas as pd
def f(x):
    return x.split('：')[-1].replace(' ','')
t=time.clock()
f1=r'C:\Users\Administrator\Desktop\11.xls'
f2=r'C:\Users\Administrator\Desktop\11.csv'
f3=r'C:\Users\Administrator\Desktop\11.txt'
f4=r'C:\Users\Administrator\Desktop\shangpin.csv'
f5=r'C:\Users\Administrator\Desktop\dingdan.csv'
try:
    a=pd.read_csv(f2,encoding='gb18030',header=None)
    r=a[a.ix[:,0].isin([str(i) for i in range(99)])].ix[:,[1,2,6]]
#同一个订单购买超过98种商品会出错
    z=r.groupby([1,2])
    b=a[a.ix[:,0].str.contains('订单号').fillna(False)].ix[:,[0,2,7,8]]
    b[5]=np.array(a.ix[b.index+1,0])
    b.sort_values([2,5],inplace=True)
    for i in b.columns:
        b[i]=b[i].map(f)
    
    try:
        z.count().to_csv(f4,header=None)
        b.to_csv(f5,header=None,index=None)
        print('操作完成,耗时{}秒'.format(time.clock()-t))
    except PermissionError as e:
        print('请先关闭shangpin.csv和dingdan.csv')
        
except FileNotFoundError as e:
    print(e)
    print('没有找到源文件')



