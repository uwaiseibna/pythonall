import json
import urllib.request, urllib.parse, urllib.error
import re
sum=0
url= input()
fhand= urllib.request.urlopen(url)
data = fhand.read().decode()
print(data)
info = json.loads(data)
#print('User count:', len(info['comments']))
for i in info['comments']:
    a= i['count']
    sum=sum+int(a)

print(sum)
