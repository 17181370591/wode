#c:
#cd C:\Users\Administrator\Desktop\1\proj
#celery -A www worker -l info  -P eventlet

import time
from celery import Celery
app = Celery('www',
             backend='redis://:asd123@localhost:6379')
app.config_from_object('celeryconfig')

@app.task  #普通函数装饰为 celery task
def add(x, y):
    time.sleep(4)
    return x + y

def f():
    r=add.delay(2,5)
    while not r.ready():
        print('*'*8)
        time.sleep(1)
    print(r.get())
