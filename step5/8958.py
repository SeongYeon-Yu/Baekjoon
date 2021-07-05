n = int(input())
for i in range(n):
  a = input()
  s = list(a)
  score = 0
  c = 1
  for i in s:
    if i == 'O':
      score+=c
      c+=1
    else:
      c=1
  print(score)