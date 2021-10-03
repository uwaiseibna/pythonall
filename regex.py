import re

fh= input('Enter file name: ')
f= open(fh)
y=list()
x=list()

for line in f:
    line = line.rstrip()
    y =re.findall('[0-9]+', line)
    print(y)
    if len(y)>0 :
        for i in range(len(y)):
            x.append(int(y[i]))

print(x,sum(x))
