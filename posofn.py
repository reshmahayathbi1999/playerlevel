m,n=map(int,input().split())
a1=list(map(int,input().split()))
c=m-1
for i in a1:
  if(a1[i]==n):
    c=i
print(c+1)
