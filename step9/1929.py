m, n = map(int, input().split())

exp = set()
primes = []
for i in range(2, n+1):
    if i in exp:
        continue
    if i >= m:
        primes.append(i)
    j = 1
    while i * j <= n:
        exp.add(i*j)
        j+=1
print("\n".join(map(str, primes)))