#!/user/bin/env python
#-*-coding:utf-8-*-
#time:2019/3/30

def w_args(*args1):
    def w(f):
        def inner(*args,**kwargs):
            print(*args1,end="\t")
            return f(*args,**kwargs)
        return inner
    return w

@w_args('f1','---')
def f1(a,b):
    return a+b

@w_args((1,2),[3,4],{5:6})
def f2(a,b,c):
    return a+b+c

@w_args()
def f3(a):
    pass

print(f1(1,2))          #f1 ---	3
print(f2(3,4,5))        #(1,2),[3,4],{5:6}
print(f3(5))            #	None
