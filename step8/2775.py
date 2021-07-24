T = int(input())

for i in range(T):
  K = int(input())
  N = int(input())
  p = [i for i in range(1, N+1)]

  for x in range(K):
    for y in range(1, N):
      p[y] += p[y-1]
  print(p[-1])