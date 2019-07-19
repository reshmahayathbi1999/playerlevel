n=int(input())
l1=[]
count=0
while(n>0):
    rem=n%10
    l1.append(rem)
    n=n//10
for i in range(len(l1)):
    if(l1.count(l1[i])>1):
        count+=1
        break
if(count==1):
    print("yes")
else:
    print("no")
