import sys,sqlite3
conn=sqlite3.connect(r'c:\python34\sb.db')
cur=conn.cursor()
cur.execute('''CREATE TABLE fffd(
na TEXT PRIMARY KEY,
aa FLOAT,
bb FLOAT)
''')
qu='INSERT INTO fffd VALUES(?,?,?)'
def co(i):
    if i.startswith('~'):
        return i.strip('~')
    if not i:
        i='0'
    return float(i)
ss=[]
t=open(r'c:\python34\ttt.txt')
for i in t:
    ss=[co(j) for j in i.split('^')]
 #   print(ss[1],ss[2],ss[3])
    cur.execute(qu,[ss[0],ss[1],ss[2]])
conn.commit()
conn.close()
