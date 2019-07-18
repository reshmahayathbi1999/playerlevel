s1,s2=input().split()
s1=s1.lower()
s2=s2.lower()
Flag1=False
if len(s1)==len(s2):
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            flag1=True
        else:
            
            flag1=False
            break
else:
    flag1=False        
if flag1==True:
    print("yes",end='')
else:
    print("no",end='')        
