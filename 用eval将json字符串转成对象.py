import re,json,time

#使用json.loads转不了可以用eval
a='[(1,2),(3,4)]'
ea=eval(a)
print(ea[0],ea[1][-1])              #(1, 2) 4

a='{"b":"c","d":["d1","d2"]}'
ea=eval(a)
print(ea['b'],ea['d'][-1])          #c d2



s1='["x1x","x2x","x3x","x打算x"],'*80
s2='["a1a","b2b","c3c","d打算d"]'
s='['+s1+s2+']'

#速度测试，即使返回json，数据多也用re，re是对数级别，其他线性

c=10**4

t=time.clock()
p1=re.compile('a(.*?)a')
p2=re.compile('b(.*?)b')
p3=re.compile('c(.*?)c')
p4=re.compile('d(.*?)d')
for i in range(c):
    a=re.search(p1,s).group(0)
    b=re.search(p2,s).group(0)
    e=re.search(p3,s).group(0)
    d=re.search(p4,s).group(0)
print(time.clock()-t)               #10次0.08，20次0.09，40次0.1


t=time.clock()
for i in range(c):
    x=json.loads(s)
    a,b,e,d=x[0],x[1],x[2],x[3]
print(time.clock()-t)               #10次0.09，20次0.14，40次0.28

t=time.clock()
for i in range(c):
    x=eval(s)
    a,b,e,d=x[0],x[1],x[2],x[3]
print(time.clock()-t)               #10次1.00，20次1.85，40次3.75
