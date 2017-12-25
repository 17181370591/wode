def sc(s):
    try:
        try:
            s+''
        except TypeError:
            pass
        else:
            raise TypeError    
        for i in s:
            for ii in sc(i):
                yield ii
    except TypeError:
        yield s
        
#a=[[1,2],[3,[4,[[5,6],7]]],8]
a=[['1','2'],['3',['4','5']],'6']        
print(list(sc(a)))
