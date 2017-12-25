#try:
while True:
    try:
        a=input('a')
        b=input('b')
        a=single(a)
        b=int(b)
        print (a/b)
    except TypeError as e:
        print(e)
#print(a/b)
#except      
