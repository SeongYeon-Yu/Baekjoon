n = int(input())
for i in range(n):
  cnt, s  = input().split()
  for j in s:
    print(j*int(cnt), end = '')
  print()
