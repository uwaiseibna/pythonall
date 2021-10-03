n=int(input())
d=[]
f=[]
t={}
count =1
cnt=0
for i in range(0,n):
    val= input()
    d.append(val)
for i in d:
    if(i in t):
        t[i]=t[i]+1
        f.append(i+str(t[i]-1))
    else:
        t[i]=1
        f.append("OK")
for i in f:
    print(i)