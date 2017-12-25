import fileinput
import re
#ff=fileinput.input([r'c:\Python34\123.txt',r'c:\Python34\新建 文本文档 (2).txt'])
ff=fileinput.input(r'c:\Python34\123.txt')
p=re.compile(r'\[([a-z0-9]+@[a-z0-9]+)\.[a-z0-9]+\]',re.IGNORECASE)
jj=[]
for j in ff:
    jj.append(j)
jj=repr(jj)

#print(jj) 
    

#print(re.search(p,jj).group(1).replace('-','/'))
print(re.sub(p,r'ni\1hao',jj))
