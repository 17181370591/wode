import urllib

#这种%[0-9a-z]是url编码。
print(urllib.parse.unquote('%3D%E5%85%AC%E5%8F%B8'))
>>>'=公司'
