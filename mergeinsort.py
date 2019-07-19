m,n=map(int,input().split())
a=list(map(int,input().split()))
b1=list(map(int,input().split()))
for i in b1:
  a.append(i)
a.sort()
print(*a,end=" ")
