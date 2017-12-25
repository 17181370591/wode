def lines(file):
    for line in file:
        yield line
        yield '\n'
def blocks(file):
    block=[]
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block=[]
a=open(r'c:\python34\ttt.txt')
for i in blocks(a):
    print(i)
##for i in lines(a):
  #  if i.strip():
   #     print(i.strip(),'yyyyyy')
    #else:
         #   print(i.strip(),'dddd')
  
    
