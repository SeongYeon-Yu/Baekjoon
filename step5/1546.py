n = int(input())
a = list(map(int, input().split()))
new = []
for i in a:
  new.append(i/max(a) * 100)
avg = sum(new)/n
print(avg)