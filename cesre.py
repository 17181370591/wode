import re
t=r'<spanclass="red">I am your faithful slave and to you <span class="green">'
#t='aaaaaaaaaasdddddddddd'
p=re.compile(r'<[^>g<]*>')
#p=re.compile(r'^(?![12]).*$')
pp=p.findall(t)
for i in pp:
    print(i)
