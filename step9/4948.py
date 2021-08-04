import math

def isPrime(num):
    if num == 1: return False #1은 소수 x

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False

    return True


while(1):
    cnt = 0 # 소수갯수
    n = int(input())
    if n == 0: break

    for i in range(n+1, 2*n+1):
        if isPrime(i):
            cnt += 1

    print(cnt)