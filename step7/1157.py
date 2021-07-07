s = input().upper()

al = {}

for i in s:
  if i in al:
    al[i] +=1
  else:
    al[i] = 1
  
ans = 0
big = 0

for i in al:
  if al[i]>big:
    big = al[i]
    ans = i
  elif al[i]==big:
    ans = "?"

print(ans)