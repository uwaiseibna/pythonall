import urllib.request, urllib.parse, urllib.error
import re
fhand= urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')
x=list()

dic= dict()

for line in fhand:
    line= line.decode()
    print(line)
    y= line.split('0-9')
    w= re.findall('[0-9+]', y)
    print(w)
    #type(y)
