inp11=int(input())
for j in range(2,inp11+1):
  if(inp11%j==0):
      inp2=0
      for m in range(2,j+1):
          if(j%m==0) and (m!=j):
              inp2=1
              break
      if(inp2==0):
          print(j,end=' ')
