

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
i=0
a= list()
url = input('Enter - ')

while i<7:
       html = urllib.request.urlopen(url, context=ctx).read()
       soup = BeautifulSoup(html, 'html.parser')
       tags = soup('a')
       for tag in tags:
            x=tag.get('href')
            a.append(x)
       url= a[17]
       if i <6:
           a.clear()
       i=i+1
print(a[17])
