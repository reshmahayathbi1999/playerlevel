l=list(map(int,input().split()))
o1=l[len(l)-1]
f=[i for i in input().split()]
for i in f:
    if f.count(i)==o1:
        print(i)
        break
