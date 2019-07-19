ni=int(input())
z=list(map(int,input().split()))
zz=list(map(int,input().split()))
z=set(z)
zz=set(zz)
if(z & zz):
  c1=sorted(z&zz)
  print(*c1,sep=' ')
