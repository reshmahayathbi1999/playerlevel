import math
anglee=int(input())
b=math.radians(anglee)
y=math.sin(b)
if(b<1):
    print(round(y,1))
elif(b>1):
    print(round(y))
