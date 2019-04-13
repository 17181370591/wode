
#https://blog.csdn.net/seetheworld518/article/details/49639651

import time
from multiprocessing import Pool as P1
from multiprocessing.dummy import Pool as P2
def run(fn):
  #fn: 函数参数是数据列表的一个元素
  time.sleep(1)
  print(fn*fn)
  return fn*fn

if __name__ == "__main__":
  testFL = [1,2,3,4,5,6]  
  print ('concurrent:') #创建多个进程，并行执行
  pool = P1(5)  #创建拥有5个进程数量的进程池
  #pool=P2(5)
  #testFL:要处理的数据列表，run：处理testFL列表中数据的函数
  
  
  
  #第一种获取返回值的方法，得到的是值
  rl =pool.map(run, testFL) 
  pool.close()#关闭进程池，不再接受新的进程
  pool.join()#主进程阻塞等待子进程的退出
  print (r1)
  for  i in r1:
    print(i)
    
  #第二种获取返回值的方法，得到的是applyresult对象
  '''
  r1=[ pool.apply_async(run,(i,)) for i in testFL ]
  #pool1.apply_async不阻塞，pool1.apply阻塞  
  pool.close()#关闭进程池，不再接受新的进程
  pool.join()#主进程阻塞等待子进程的退出
  print (r1)
  for  i in r1:
    print(i.get())
  '''
