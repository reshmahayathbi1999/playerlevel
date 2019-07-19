n=int(input())
li=[]
l=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if(l[i]>l[j]):
            d=l[i]-l[j]
        else:
            d=l[j]-l[i]
        li.append(d)
print(max(li))
