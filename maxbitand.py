n=int(input())
a=list(map(int,input().split()))
b1=[]
for i in range (n):
  for j in range(0,n):
    b1.append(a[i] & a[i])
print(max(b1))
