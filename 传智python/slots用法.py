#!/user/bin/env python
#-*-coding:utf-8-*-
#time:2019/3/30
import types
class P:
    __slots__ = ('a','b')
    c = 4
def f(self):
    print(self.a+6)
p1=P()
p1.a=3
print(p1.a,p1.c)
xx=types.MethodType(f,p1)
p1.z=xx
p1.b()