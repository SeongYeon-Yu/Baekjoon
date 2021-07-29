M = int(input())
N = int(input())

lst = []
for i in range(M,N+1):
  k = 0
  if i>1:
    for j in range(2,i):
      if i % j == 0:
        k+=1
        break
    if k ==0:
      lst.append(i)

if len(lst)>0:
  print(sum(lst))
  print(min(lst))
else:
  print(-1)