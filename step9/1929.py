m, n = map(int, input().split()) #

exp = set() #제외대상 수를 만들 집합체
primes = [] #소수 리스트
for i in range(2, n+1):
    if i in exp:
        continue #제외대상이라면 continue
    if i >= m: 
        primes.append(i)
    j = 1
    while i * j <= n:
        exp.add(i*j)
        j+=1
print("\n".join(map(str, primes)))