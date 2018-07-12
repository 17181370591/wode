#https://blog.csdn.net/qq_28219759/article/details/52919233
import pandas as pd,numpy as np

p=pd.DataFrame(np.arange(1,73).reshape(9,8),index=list('abcdefghi'))
p.columns=['a{}'.format(i) for i in range(1,9)]


#删除h行
q.drop('h')
#删除a4列
q.drop('a4',axis=1)
#可以发现q没有变化，即返回了q的副本
print(q)


#删除ehd三行，原地修改
q.drop(['e','h','d'],inplace=True)



#is_unique是Series的属性，返回该行/列是否有相同值
#存在None或者np.NAN也返回false
q.loc['b',:].is_unique



#Series的str属性
q.a1=q.a1.map(str)      #将a1列转str
q.a1.map(type)      #可以发现所有值都是str
'''
>> q.a1.str.cat(list('123456'),sep='+')
a      1+1
b    asd+2
c     17+3
f     41+4
g     49+5
i     65+6
'''
#上面直接用q.a1.cat(list('123456'),sep='+')会报错



#s.str有时会将s的值全部转成str格式，有时不会，原因不明
#似乎要求s不能全部为int/float，需要有str
s = pd.Series(['a_b_c', 'c_d_e', np.nan,123])
s.str.split('_')
'''
>>> s.str.split('_')
0    [a, b, c]
1    [c, d, e]
2          NaN
3          NaN
dtype: object
'''

'''
#返回s的每个值的第i个字符，没有则返回None
s.str.get(i)
contains() 是否包含表达式
replace() 替换
repeat() 重复
pad() 左右补齐
center() 中间补齐，看例子
ljust() 右边补齐，看例子
zfill() 左边补0
count() 计算给定单词出现的次数
startswith() 判断是否以给定的字符串开头
endswith() 判断是否以给定的字符串结束
findall() 查找所有符合正则表达式的字符，以数组形式返回
match() 检测是否全部匹配给点的字符串或者表达式
len() 计算字符串的长度
trip() 去除前后的空白字符
extract() 抽取匹配的字符串出来，注意要加上括号，把你需要抽取的东西标注上
lower() 全部小写
#find找不到返回-1，本身是None的话返回None（np.NAN）
find() 从左边开始，查找给定字符串的所在位置
index() 查找给定字符串的位置，注意，如果不存在这个字符串，那么会报错！
swapcase() 大小写互换
isalnum() 是否全部是数字和字母组成
isalpha() 是否全部是字母
isdigit() 是否全部都是数字
isspace() 是否空格
islower() 是否全部小写
istitle() 是否只有首字母为大写，其他字母为小写
isnumeric() 是否是数字
isdecimal() 是否全是数字

'''
np.lexsort
#https://www.cnblogs.com/liyuxia713/p/7082091.html
lexsort支持对数组按指定行或列的顺序排序；是间接排序，lexsort不修改原数组，返回索引。
（对应lexsort 一维数组的是argsort a.argsort()这么使用就可以；argsort也不修改原数组， 返回索引）
 
默认按最后一行元素有小到大排序, 返回最后一行元素排序后索引所在位置。
设数组a, 返回的索引ind，ind返回的是一维数组
对于一维数组, a[ind]就是排序后的数组。
对于二维数组下面会详细举例。
 
import numpy as np
 
>>> a
array([[ 2,  7,  4,  2],
       [35,  9,  1,  5],
       [22, 12,  3,  2]])
 
按最后一列顺序排序
>>> a[np.lexsort(a.T)]
array([[22, 12,  3,  2],
       [ 2,  7,  4,  2],
       [35,  9,  1,  5]])
 
按最后一列逆序排序
>>>a[np.lexsort(-a.T)]
array([[35,  9,  1,  5],
       [ 2,  7,  4,  2],
       [22, 12,  3,  2]])
 
按第一列顺序排序
>>> a[np.lexsort(a[:,::-1].T)]
array([[ 2,  7,  4,  2],
       [22, 12,  3,  2],
       [35,  9,  1,  5]])
 
按最后一行顺序排序
>>> a.T[np.lexsort(a)].T
array([[ 2,  4,  7,  2],
       [ 5,  1,  9, 35],
       [ 2,  3, 12, 22]])
 
按第一行顺序排序
>>> a.T[np.lexsort(a[::-1,:])].T
array([[ 2,  2,  4,  7],
       [ 5, 35,  1,  9],
       [ 2, 22,  3, 12]])


==========================================================================================

#hsplit和vsplit，分别用来水平/竖直切割array，
#参数是整数时按比例切分，是列表时按索引切分

>>> a=np.arange(36).reshape(6,6)

>>> np.vsplit(a,[1,3,4])
[array([[0, 1, 2, 3, 4, 5]]), array([[ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17]]), array([[18, 19, 20, 21, 22, 23]]), array([[24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])]

>>> np.vsplit(a,[2])
[array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]]), array([[12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])]

>>> np.vsplit(a,3)
[array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]]), array([[12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]]), array([[24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])]


