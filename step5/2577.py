A = int(input())
B = int(input())
C = int(input())
result = A*B*C
result = str(result)
cnt = 0
for i in range(0,10):
  print(result.count(str(i)))