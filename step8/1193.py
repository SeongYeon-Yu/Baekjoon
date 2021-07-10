x = int(input())
a = 1
while x>a:
  x-=a
  a+=1

if a%2 ==0:
  b=x
  c=a-x+1
else:
  b = a-x+1
  c=x
print(b,'/', c, sep = '')