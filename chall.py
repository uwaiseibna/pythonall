list= ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
bool=True
for i in list:
    li=i.split(' ')
    l=len(li[0])
    m=len(li[2])
    n=l-m
    if (len(li)>5):
        print('Error: Too many problems.')
    elif (li[1] != '-' or li[1] != '+'):
        print ("Error: Operator must be '+' or '-'.")
    try:
        s=int(li[0]) +int (li[2])
    except:
        print('Error: Numbers must only contain digits.')
    if (l>4 or m>4):
        print('Error: Numbers cannot be more than four digits.')
    if n>0:
        print(' ',li[0])
        print(li[1],' '*(n-1),li[2])
        print('-'*(l+2))
        if bool== True:
            print(' ',int(li[0])+int(li[2]))
    else:
        print(' '*(abs(n)+1),li[0])
        print(li[1],li[2])
        print('-'*(m+2))
        if bool ==True:
            print(' ',int(li[0])+int(li[2]))
