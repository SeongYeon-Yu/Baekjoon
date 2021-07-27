N = int(input())
a = list(map(int, input().split()))
cnt = 0

if len(a) == N:
  for i in a:
    b = 0
    for j in range(1, i+1):
      if i % j == 0:
        b +=1
    if b ==2 :
      cnt+=1
print(cnt)