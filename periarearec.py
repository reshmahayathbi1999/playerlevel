a1,b=map(int,input().split())
c=(a1//2)-1
for i in range(1,c+1):
  if(i*c==b):
    print("yes")
    break
  else:
    c=c-1
else:
  print("no")
