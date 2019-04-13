#!/user/bin/env python
#-*-coding:utf-8-*-
#time:2019/3/30

#元类type，用来创建类

class Q:
    b=2

def f(self):
    print('--f--{}--'.format(self.a))

P=type('P',(Q,),{'a':1,'ff':f})
print(P)            #<class '__main__.P'>
p=P()
print(p)            #<__main__.P object at 0x0000000000693240>
print(p.a,p.b)      #1 2
p.ff()              #--f--1--

print(p.__class__)  #<class '__main__.P'>
print(P.__class__)  #<class 'type'>
print(Q.__class__)  #<class 'type'>