def arrprod(n):
    s=len(n)-1
    if not n:
        return 1
    else:
        s-=1
        return n[s]* arrprod(n)