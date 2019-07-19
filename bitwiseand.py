n=int(input())
l=[int(i) for i in input().split()]
r1=l[0]
for i in range(1,n):
    r1=r1&l[i]
print(r1)
