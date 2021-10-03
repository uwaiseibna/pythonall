

def arithmetic_arranger(problems):
  lst=[]
  arranged_problems=[]
  for i  in range (0, len(problems)):
        lst.append(problems[i])
    
        for a in lst[i].split():
            try:
                 arranged_problems.append(int(a))
            except:
                 arranged_problems.append(a)
  for i in arranged_problems:
       print(i)
        
    


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))