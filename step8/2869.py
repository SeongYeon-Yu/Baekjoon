a,b,v = map(int, input().split())
q = 0
if (v-b) % (a-b)!=0:
  q = ((v-b)//(a-b))+1
else:
  q = ((v-b)//(a-b))
print(q)