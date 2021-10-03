name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
lst= list()
lst2=list()
dic= dict()
lst3=list()
for line in fh:
    line= line.rstrip()
    if line.startswith('From'):
        a= line.split()
        if len(a)>6:
            lst.append(a[5])
for l in lst:
    l=l.split(':')
    lst2.append(l[0])
for a in lst2:
    dic[a]= dic.get(a,0)+ 1

tup=dic.items()
c=sorted(tup)
for s,t in c:
    print (s,t)
