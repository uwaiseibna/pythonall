marks={}

participants=int(input())
total=0
for i in range(1,participants+1):
    sum=0
    for j in range(0,3):
        score = (int(input()))
        sum=sum+score
        total=total+score
    marks[i]=sum
marks
marklist = sorted(marks.items(), key=lambda x:x[1],reverse=True)
sortdict = dict(marklist)

for i in range(1,participants+1):
    
    print("Participant"+str(i)+' =',list(sortdict.keys()).index(i)+1)
    

print("Partcipant"+str(list(sortdict.keys())[0] )+" scored top = ",sortdict[list(sortdict.keys())[0]])    
print("Partcipant"+str(list(sortdict.keys())[-1] )+" scored lowest = ",sortdict[list(sortdict.keys())[-1]])

    
print("Avg score=",total/participants)