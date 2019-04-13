#!/user/bin/env python
#-*-coding:utf-8-*-
#time:2019/3/30

def w(f):
    def inner(*args,**kwargs):
        print('i'*11,end="\t")
        return f(*args,**kwargs)
    return inner

@w
def f1(a,b):
    return a+b

@w
def f2(a,b,c):
    return a+b+c

@w
def f3(a):
    pass

print(f1(1,2))          #iiiiiiiiiii	3
print(f2(3,4,5))        #iiiiiiiiiii	12
print(f3(5))            #iiiiiiiiiii	None
