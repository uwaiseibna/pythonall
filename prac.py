list=[]
for i in range(1,50):
    list.append(i)
list=sorted(list)
mid=int(len(list)/2)
while(list[mid]!=5):
    if (5>=mid):
        list=list[mid:]
    elif(5<mid):
        list=list[:mid]
    mid=int (len(list)/2)

print(list[mid])