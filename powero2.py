import math
N=int(input())
a1=math.log(N,2)
if math.ceil(a1)==math.floor(a1):
    print("yes")
else:
    print("no")
