n = int(input())
li = list(map(int,input().split()))
c1 = 1
count = []
for i in range(n-1):
  if li[i] < li[i+1]:
    c1 += 1
  else:
    c1= 1
    continue
  count.append(c1)
print(max(count))
