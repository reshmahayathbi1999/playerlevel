import string
a1=input()
a1.split()
a1=a1.replace(" ","")
b=[i for i in a1 if a1.count(i)==1]
c=' '.join(b)
print(c.lower())
