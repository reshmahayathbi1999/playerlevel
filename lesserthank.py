l,m=map(int,input().split())
t=list(map(int,input().split()))
p=[]
for i in t:
    if(i<m):
        p.append(i)
y1=sorted(p)
print(*y1)
