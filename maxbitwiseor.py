n=int(input())
l=[int(i) for i in input().split()]
r1=[]
for i in range(n):
    for j in range(n):
        t=l[i]|l[j]
        r1.append(t)
print(max(r1))
