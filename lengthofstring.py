num1=input()
lis1=[]
s1=""
r=0
for i in range(0,len(num1)):
    for j in range(i,len(num1)):
        s1=s1+num1[j]
        if(s1[::-1]==s1):
            r=len(num1)-len(s1)
            lis1.append(r)
    s1=""
print(min(lis1))
