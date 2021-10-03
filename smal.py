dic={'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

for key in dic:
    dic[key]= dic[key]-1
print(dic)
for a in dic:
    dic[a]= dic.get(a,0)+1
largest= -1
word= None
for k,v in dic.items():
    if v>largest:
        largest=v
        word=k
print(word,largest)
