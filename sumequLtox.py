a1,b=map(int,input().split())
o=list(map(int,input().split()))
v=0
for i in range(0,len(o)):
    for j in range(1,len(o)):
        sum=o[i]+o[j]
        if sum==b:
            v=1
if v==1:
    print("yes")
else:
    print("no")
