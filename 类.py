class Bird:
    
    def __init__(s):
    	s.duzi=False
	
    def eat(s,sw='树叶'):
        if s.duzi:
            print('我不吃')
        else:
            print(sw+'很好吃')
            s.duzi=True

    def play(s,wj='蛋'):
            s.duzi=False
            print(wj+'真好玩')

class T(Bird):
    def __init__(s):
        super(T,s).__init__()
        s.xq=True
    def j(s,cishu=3):
        if s.xq:
            t='汪'
        else:
            t='喵'
        print(t*cishu)    
        s.zh()
    def zh(s):
        if s.xq==True:
            s.xq=False
        else:
            s.xq=True
        
