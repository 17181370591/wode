def cctt(state,wz):
    y=len(state)
    for i in range(y):
        if abs(state[i]-wz) in (0,y-i):
            return True
    return False    
def ffhh(num,state=()):
    for i in range(num):
             if not cctt(state,i):
                if len(state)==num-1:
                    yield (i,)
                else:
                      for j in ffhh(num,state+(i,)):
                        yield (i,)+j

def fh(num,place=[]):
    for i in range(num):
             if not cctt(place,i):
                if num==len(place)+1:
                    yield [i]
                else:
                    for j in fh(num,place+[i]):
                        yield [i]+j                        
def pp(li):
    for i in range(len(li)):
        for j in range(len(li[i])):
            print('o'*li[i][j]+'x'+'o'*(len(li[i])-1-li[i][j]))
        print('-'*11)    
def qq(li):
    for i in li:
        print(i)
def www(i):
    pp(list(fh(i)))        
    print(list(fh(i)))
    print(len(list(fh(i))))


www(5)
