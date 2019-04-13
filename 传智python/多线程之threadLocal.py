import threading,time

# 创建全局ThreadLocal对象:
tl = threading.local()

def process_s():
    # 获取当前线程关联的s:
    std = tl.s
    name=threading.current_thread().name
    print('{} in {}'.format(std, name))

def process_thread(name):
    # 绑定ThreadLocal的s:
    print(tl)
    tl.s = name
    process_s()

t1 = threading.Thread(target= process_thread, args=('dog',), name='Thread-A')
t1.start()

t2 = threading.Thread(target= process_thread, args=('cat',), name='Thread-B')
t2.start()


'''
<_thread._local object at 0x00000000029F7150>
dog in Thread-A
<_thread._local object at 0x00000000029F7150>
cat in Thread-B
'''
