N = int(input())
a = list(map(int, input().split()))
cnt = 0 #소수개수

if len(a) == N: 
  for i in a:
    b = 0 #나뉘는 수 갯수
    for j in range(1, i+1): #i를 j로 나눌건데, 1부터 i까지의 수로 다 나누어본다.
      if i % j == 0: #나누어떨어지면
        b +=1 #나뉘는 수 갯수를 1증가
    if b ==2 : #나뉘는 수가 2개일시 소수이므로
      cnt+=1 #소수개수를 1증가
print(cnt)