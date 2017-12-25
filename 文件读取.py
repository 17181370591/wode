r=[]
with open(r'c:\python34\123.txt','r') as e:
    for i in e.readlines():
        r.append(i.strip())
#print(r)
print(r'"%s:%s","%s:%s","%s:%s","%s:%s","%s:%s"' %tuple(r))

