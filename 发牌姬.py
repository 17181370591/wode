from random import *
#def 洗牌():
 #   pai=[]
  #  shu=list(range(1,11))+['j','q','k']
   # hua=['方片','梅花','红桃','黑桃']
    #for i in shu:
     #   for j in hua:
      #      pai.append(j+str(i))
    #return shuffle(pai)#
#def 发牌(pai):
#    while len(pai):        
#        input('你获得的牌是：'+pai.pop())
#pai=洗牌()
pai=[]
shu=list(range(1,11))+['j','q','k']
hua=['方片','梅花','红桃','黑桃']
for i in shu:
    for j in hua:
        pai.append(j+str(i))
shuffle(pai)
while len(pai):        
    input('你获得的牌是：'+pai.pop())
