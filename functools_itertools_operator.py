import functools,itertools,operator


#cmp_to_key:比较函数
key1=functools.cmp_to_key(lambda x,y:x%3-y%3)
key2=functools.cmp_to_key(lambda x,y:d[x]-d[y])
a=[1,8,4,6,2]
print(sorted(a,key=key1))
#=>[6, 1, 4, 8, 2]
d={'a':3,'b':1,'c':6}
print(sorted(d,key=key2))
#=>['b', 'a', 'c']


#partial:冻结部分函数位置函数
def say(a,b):
    print(a,b)
nya=functools.partial(say,b='nya!!!')
nya('good')
#=>good nya!!!


#reduce:两个参数的function从左至右依次作用于序列中的项，减少序列为单个值
nya=functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(nya)
#=>15


#count:count(start=0, step=1) 会返回一个无限的整数iterator，每次增加1。可以选择提供起始编号，默认为0。
for i in zip(itertools.count(start=0,step=1), ['a', 'b', 'c']):
    print(i, end='#')
#=>(0, 'a')#(1, 'b')#(2, 'c')#


#cycle:cycle(iterable) 会把传入的一个序列无限重复下去，不过可以提供第二个参数就可以制定重复次数。
for i in zip(range(7), itertools.cycle(['a', 'b', 'c'])):
    print(i, end='#')
#=>(0, 'a')#(1, 'b')#(2, 'c')#(3, 'a')#(4, 'b')#(5, 'c')#(6, 'a')#


#accumulate:对序列前所有项累计计算
a=list(range(1,6))
b=list(itertools.accumulate(a))
c=list(itertools.accumulate(a,func=operator.mul))
print(a,b,c)
#=>[1, 2, 3, 4, 5],[1, 3, 6, 10, 15],[1, 2, 6, 24, 120]


#product(iter1,iter2, ... iterN, [repeat=1]);创建一个迭代器，生成表示item1，
# item2等中的项目的笛卡尔积的元组，repeat是一个关键字参数，指定重复生成序列的次数
a=itertools.product('ABCD', 'xy')
print(list(a))
#=>[('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]
a=itertools.product(range(2), repeat=3)
print(list(a))
#=>[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
a=list(itertools.product('AB', 'xy', repeat=2))
print(len(a),a)
#=>16 [('A', 'x', 'A', 'x'), ('A', 'x', 'A', 'y'), ('A', 'x', 'B', 'x'), ('A', 'x', 'B', 'y'),
#  ('A', 'y', 'A', 'x'), ('A', 'y', 'A', 'y'), ('A', 'y', 'B', 'x'), ('A', 'y', 'B', 'y'),
# ('B', 'x', 'A', 'x'), ('B', 'x', 'A', 'y'), ('B', 'x', 'B', 'x'), ('B', 'x', 'B', 'y'),
# ('B', 'y', 'A', 'x'), ('B', 'y', 'A', 'y'), ('B', 'y', 'B', 'x'), ('B', 'y', 'B', 'y')]


#permutations(iterable, r=None)返回长度为r的所有可能的组合，每个项看做不同项，即使值相等
a=list(itertools.permutations('aba'))
print(len(a),a)
#=>6 [('a', 'b', 'a'), ('a', 'a', 'b'), ('b', 'a', 'a'), ('b', 'a', 'a'), ('a', 'a', 'b'), ('a', 'b', 'a')]
a=list(itertools.permutations(('a','b','c'),2))
print(len(a),a)
#=>6 [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
def queen8(x):       #八皇后问题的一种写法
    p=itertools.permutations(range(x))
    for i in p:
        if x==len(set((i[j]+j for j in i))) and x==len(set((i[j]-j for j in i))):
            print(i)
            for a in i:
                z=['o']*x
                z[a]='x'
                print(''.join(z))


#groupby可以自动将一个序列分组，相同相邻的元素会归为一组，形成一个新的生成器
a=itertools.groupby('aasssa')
for key, group in a:
    print(key,'-->',list(group),end='   ')
#=>a --> ['a', 'a']   s --> ['s', 's', 's']   a --> ['a']


#combinations(iterable, r) 返回一个iterator，提供iterable中所有元素可能组合的r元组。
# 每个元组中的元素保持与iterable返回的顺序相同。
#combinations_with_replacement(iterable, r)函数放宽了一个不同的约束：
# 元素可以在单个元组中重复，即可以出现aa/bb/cc/dd等组合
a=list(itertools.combinations('abcd',r=3))
print(len(a),a)
#=>4 [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
a=list(itertools.combinations_with_replacement(('a','b','c'),2))
print(len(a),a)
#=>6 [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]


#deque:使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
deque(['y', 'a', 'b', 'c', 'x'])
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
# 这样就可以非常高效地往头部添加或删除元素。

#defaultdict:当key不存在时，返回默认值
q=collections.defaultdict(lambda: 'haha')
q[3]=33
for i in range(4):
    print(q[i],end='    ')
#=》haha    haha    haha    33
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = collections.defaultdict(set)                #让值是一个集合
for k, v in s:
    d[k].add(v)
print(d.items())
#=>dict_items([('red', {1, 3}), ('blue', {2, 4})])


#OrderedDict:使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
#=>{'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#=>OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
od.keys() # 按照插入的Key的顺序返回
#=>['z', 'y', 'x']


#Counter:
d='progr ammm'
q=collections.Counter(d)
print(q)
#=>Counter({'m': 3, 'r': 2, 'p': 1, 'o': 1, 'g': 1, ' ': 1, 'a': 1})
q.update(' '*3)                     #对集合进行并集更新
print(q)
q.subtract('am3')                   #对集合做减法
print(q)
#=>Counter({' ': 4, 'r': 2, 'm': 2, 'p': 1, 'o': 1, 'g': 1, 'a': 0, '3': -1})
#=>Counter({' ': 4, 'm': 3, 'r': 2, 'p': 1, 'o': 1, 'g': 1, 'a': 1})
print(q.most_common(3))             #频率最高的3项
#=>[('m', 3), ('r', 2), ('p', 1)]


#fromkeys:
seq = ('name', 'age', 'sex')
d = dict.fromkeys(seq)
print(d)
#=>{'name': None, 'age': None, 'sex': None}
d = dict.fromkeys(d, 10)
print(d)
#=>{'name': None, 'age': None, 'sex': None}