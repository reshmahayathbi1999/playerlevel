n,k=map(int,input().split())
l1=[int(i) for i in input().split()]
for i in range(k):
    l1.pop()
print(sep=" ",*l1)
