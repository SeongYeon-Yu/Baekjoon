T = int(input())

for i in range(T):
  K = int(input()) #층 
  N = int(input()) #호
  p = [i for i in range(1, N+1)] #아래층사람들 수

  for x in range(K): 
    for y in range(1, N):
      p[y] += p[y-1] 
  print(p[-1])