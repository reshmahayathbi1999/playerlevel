def fac(m):
    s1=1
    for i in range(1,m+1):
        s1=s1*i
    return s1
m,k=map(int,input().split())
print(fac(m)//fac(m-k))
