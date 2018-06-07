# -*- coding:utf-8 -*-
from multiprocessing import Process, Manager,Pool
import time
import random

def kkk(a_list, number):
    for i in range(10):
        a_list.append(i)
        print('这是进程{} {}'.format(number, a_list))
    print('这是进程{} {}'.format(number, a_list))

if __name__ == '__main__':
    
    #manager用来在进程之间传递/共享参数
    manager = Manager()
    a_list = manager.list()
    #如果a_list等于普通的列表，会发现数据没有共享
    #a_list = []
    
    p = Pool(2)
    #方法1：使用starmap调用函数并传递多参数
    xy=zip((a_list,a_list),range(2))
    p.starmap(kkk,xy)
    
    '''
    #方法2：使用偏函数固定一个参数，然后用普通方法传另一个参数
    from functools import partial
    kk2=partial(kkk,number=3)
    p.map(kk2,(a_list,a_list))
    '''
    p.close()
    p.join()
    print(a_list)
    print(len(a_list))
    print('it\'s ok')
