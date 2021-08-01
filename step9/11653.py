N = int(input())
for i in range(2, N):
  while N%i == 0:
    print(i)
    N //= i # 몫만 출력
if N > 1:
  print(N)