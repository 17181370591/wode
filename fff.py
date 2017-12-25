import sqlite3,sys
conn=sqlite3.connect(r'c:\python34\food.db')
curs=conn.cursor()
cur=conn.cursor()
def con(value):
    if value.startswith("~"):
        return value.strip("~")
    if not value:
        value=0
    return float(value)    
#que='create table food (id text primary key,desc text,water float,\
# kcal float,protein float,fat float,ash float,carbs float,fiber float,\
# sugar float)'
#qqq='insert into food values (?,?,?,?,?,?,?,?,?,?)'
que='select * from food'
curs.execute(que)
#for i in open(r'c:\python34\tt.txt'):
#    print([con(j) for j in i.split('^')][0:10])
#    curs.execute(qqq,[con(j) for j in i.split('^')][0:10])
p=curs.fetchall()

print(p)
print(len(p))
#cur.execute(que)
#q=curs.fetchall()
#print(q)
#print(len(q))
