from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
def convert_pdf(path, page=1):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, pageno=page,  laparams=laparams)
    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str
file  = r'C:\Users\hasee\AppData\Local\Programs\Python\Python35-32\111\1.pdf'

with open(r'C:\Users\hasee\AppData\Local\Programs\Python\Python35-32\111\1.txt','w',encoding='utf-8') as f:
    f.write(convert_pdf(file))
    
#print(convert_pdf(file))
