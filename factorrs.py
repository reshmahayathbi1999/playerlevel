k=int(input())
num=[]
for i in range (2,k+1):
    if(k%i==0 and i%2==0):
        num.append(i)
print(*num)
