from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
global page
a='''<tr>
<td><div align="right"><strong>地址：</strong></div></td>
<td>[中国  湖南  衡阳  雁峰区] 白沙洲工业园保税区综合楼102电商部</td>
<td><div align="right"><strong>邮编：</strong></div></td>
<td></td>
</tr> <tr>'''
#m= re.compile(r'地址：(.*?)\<\/td\>(.*?)\<\/td',re.S).search(a)
m= re.compile(r'地址：(.*?)</td>(.*?)</td',re.S).search(a).group(2).replace(r'<td>','')
print(m.group(2).replace(r'<td>',''))
