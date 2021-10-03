import xml.etree.ElementTree as ET

import urllib.request, urllib.parse, urllib.error
import re
sum=0
url= input()
fhand= urllib.request.urlopen(url)
print(fhand.read().decode())
fh = ET.fromstring(fhand.read())

lst= fh.findall('comments/comment/count')

for item in fh.findall('comments/comment'):
    sum= sum + int(item.find('count').text)
print(sum)
