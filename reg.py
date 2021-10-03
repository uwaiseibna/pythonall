    n = int(input())
    d = {}
    t={}
    count=1
    for i in range(0,n):
        c=i-1
        val= input()
        if val in d.values():
            val1=val+str(count)
            count=count +1
            if (val != d[c]):
                count = count-1
            
        elif val not in d.values():
            val1= 'OK'
            count =1
        t[i]=val1
        d[i]=val
    for k in t.values():
        print(k)