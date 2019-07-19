n=int(input())
a=[int(x) for x in input().split()]
b1=0
if n==len(a):
    for i in range(0,n):
        for j in range(i+1,n):
            b1=a[i]^a[j]
print(b1)
