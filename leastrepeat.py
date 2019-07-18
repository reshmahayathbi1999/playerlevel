import string
value=input()
value.split()
value=value.replace(" ","")
b=[i for i in value if value.count(i)==1]
c=' '.join(b)
print(c)
