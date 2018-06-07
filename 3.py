# -*- coding:utf-8 -*-
from multiprocessing import Process, Manager,Pool
import time
import random

from functools import partial

def kkk(a_list, number):
    for i in range(10):
        a_list.append(i)
#        time.sleep(random.randrange(2))
        print('这是进程{} {}'.format(number, a_list))
    print('这是进程{} {}'.format(number, a_list))

def kk(a,b):
    print(a+b)


if __name__ == '__main__':
    
    manager = Manager()
    a_list = manager.list()
    #a_list = []
    p = Pool(2)
    
    xy=zip((a_list,a_list),range(2))
    p.starmap(kkk,xy)
    '''
    kk2=partial(kkk,number=3)
    p.map(kk2,(a_list,a_list))
    '''
    p.close()
    p.join()
    print(a_list)
    print(len(a_list))
    print('it\'s ok')
