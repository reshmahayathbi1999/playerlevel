n=int(input())
count1=0
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if(l[i]<l[j]):
            count1+=1
print(count1)
