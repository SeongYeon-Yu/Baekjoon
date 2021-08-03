M = int(input()) # 시작숫자
N = int(input()) #마지막숫자

lst = [] # 소수를 집어넣을 리스트
for i in range(M,N+1): #M부터 N+1까지
  k = 0 #약수 계산해주는 수 
  if i>1: #i가 M부터인데, 숫자1보다 커야함 왜냐?소수는 2부터시작
    for j in range(2,i): 
      if i % j == 0: # 나머지가 0이면
        k+=1 # 약수개수 증가
        break #1이상이면 필요없으니 이프문 밖으로나가도 상관x
    if k ==0:
      lst.append(i) #lst에 소수 출력 
  
if len(lst)>0:
  print(sum(lst))
  print(min(lst))
else:
  print(-1)