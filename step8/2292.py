n = int(input())
a=1
d = 6
an = 1
if n == 1:
  print(1)
else:
  while True:
    a = a + d
    an +=1
    if n<=a:
      print(an)
      break
    d += 6