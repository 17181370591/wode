import sys,sqlite3
conn=sqlite3.connect(r'c:\python34\sb.db')
cur=conn.cursor()
cur.execute('''create table fde11(
na text ,
aa float,
bb float)
''')
qu='insert into fde11 values(?,?,?)'
def co(i):
    if i.startswith('~'):
        return i.strip('~')
    if not i:
        i='0'
    return i
for i in open(r'c:\python34\t.txt'):
    try:
        ss=[co(j) for j in i.split('^')]
      #  print(ss)
      #  print(ss[1],ss[2],ss[3])
        cur.execute(qu,[ss[1],ss[2],ss[3]])
    except IndexError as e:pass    
conn.commit()
conn.close()
