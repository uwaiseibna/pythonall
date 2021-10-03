def string_bits(str):
    str1=str[0]
    for i in range (1, len(str)):
        if(i%2==0):
            str1= str1+ str[i]
        
    print(str1)
  
  
string_bits('uwaise')

