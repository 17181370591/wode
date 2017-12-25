import  csv
cf=open(r'c:\python34\test.csv','w+')
try:
    wr=csv.writer(cf)
    wr.writerow(('number','number plus 2','number times 2'))
    for i in range(10):
        wr.writerow((i,i+2,i*2))
finally:
    cf.close()
    
