import math

def isPrime(num):
    if num == 1: return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False

    return True


while(1):
    answer = 0
    n = int(input())
    if n == 0: break

    for i in range(n+1, 2*n+1):
        if isPrime(i):
            answer += 1

    print(answer)