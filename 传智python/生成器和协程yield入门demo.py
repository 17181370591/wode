#!/user/bin/env python
#-*-coding:utf-8-*-
#time:2019/3/30

#生成器的生成方法或取值方法 和 协程yield

a=[i*2 for i in range(9) ]  #[0, 2, 4, 6, 8, 10, 12, 14, 16]
print(a)

b=(i*2 for i in range(9) )      #生成方法1
for i in b:                     #取值方法1
    print(i,end=" ")

def f():        #生成方法2
    a=2
    for i in range(9):
        x=yield a*i
        print('x={}'.format(x))
c=f()
print(c)
for i in c:                     #取值方法1
   print(i,end=" ")

c=f()
#取值方法2  next(c)和c.__next__()一样,相当于send(None)
while 1:
    try:
        print(c.__next__(),end=" ")
    except Exception as e:
        print('-'*11)
        break
c=f()
c.send(None)
while 1:        #取值方法3 send()
    #send把参数赋值给x=yield a*i的x
    try:
        print(c.send('a'),end=" ")
    except Exception as e:
        print('-'*11)
        break

def test1(x):
    while 1:
        print('--{}--'.format(x))
        yield None


t1=test1(1)
t2=test1(2)
while 1:
    next(t1)
    next(t2)