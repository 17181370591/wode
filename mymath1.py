import os,re
import xlrd,xlwt
import xlutils.copy
wz=r'c:\python34\tools'
roco=0
def bianli(weizhi):
    a=[]
    for i in os.walk(weizhi):
        if len(i[2])>0:
            for j in i[2]:
       #     print(i[0]+'\\'+j)
                if 'xls' in j:
                    a.append(i[0]+'\\'+j)
    return a
print(bianli(wz))
def fuzhi1(req):
    fn=xlwt.Workbook()
    shet=fn.add_sheet('sheets1')
    global roco
    for r in req:
        wb=xlrd.open_workbook(r)
        wsht=wb.nsheets
        nb=xlutils.copy.copy(wb)
        for t in range(wsht):
            wrow=wb.sheet_by_index(t).nrows
            wcol=wb.sheet_by_index(t).ncols
            if wrow*wcol!=0:
                for i in range(wrow):
                    for j in range(len(wb.sheet_by_index(t).row(i))):
                        shet.write(roco+i,j,wb.sheet_by_index(t).cell(i,j).value)
            roco=roco+wrow
            print(roco,'wrow:',wrow,'wcol:',wcol,'wsht:',wsht)
        fn.save(r'c:\Python34\111.xls')
def fuzhi2(req):
    fn=xlwt.Workbook()
    global roco
    for r in req:
        roco=0
        wb=xlrd.open_workbook(r)
        wsht=wb.nsheets
        pp=re.compile(r'(([^\\])*)\.xls')
        sname=re.search(pp,r).group(1)
        shet=fn.add_sheet(sname)
        nb=xlutils.copy.copy(wb)
        for t in range(wsht):
            wrow=wb.sheet_by_index(t).nrows
            wcol=wb.sheet_by_index(t).ncols
            if wrow*wcol!=0:
                for i in range(wrow):
                    for j in range(len(wb.sheet_by_index(t).row(i))):
                        shet.write(roco+i,j,wb.sheet_by_index(t).cell(i,j).value)
            roco=roco+wrow
            print(roco,'wrow:',wrow,'wcol:',wcol,'wsht:',wsht)
        fn.save(r'c:\Python34\111.xls')
def fuzhi(req,style=0):
    if style==0:
        fuzhi1(req)
    else:
        fuzhi2(req)
fuzhi(bianli(wz))   
