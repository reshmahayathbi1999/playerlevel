import math
n,sri=map(int,input().split())
a1=math.factorial(n)
b=math.factorial(n-sri)
c=math.factorial(sri)
b=b*c
print(int(a1/b))
