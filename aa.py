d=[]
c=int(input())
k=0
for i in range (0,c):
    f= input()
    d.append(f)
for j in d:
    for a in range (1,int(j)+1):
        if(int(j)%int(a)==0):
            k=k+1
    if(k==3):
        print("YES")
    else:
        print("NO")