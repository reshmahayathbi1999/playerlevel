z11=int(input())
if(z11>=-2**15+1 and z11<=2**15+1):
  print('INT')
elif(z11>=-2**31+1 and z11<=2**31+1):
  print('LONG')
else:
  print('LONG LONG')  
