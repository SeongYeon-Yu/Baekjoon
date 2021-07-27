n = int(input())

for i in range(n):
  X, Y = map(int, input().split())

  a = Y - X # 이동해야할 거리 (최대 횟수, 1만큼씩 이동시)
  cnt = 0 # 이동 횟수 (출력 값)
  k = 1 # k는 k-1, k , k+1로 1만큼 차이나므로 1로 변수설정
  m_p = 0 #총이동한거리 
  while m_p < a: #총 이동 거리가 이동해야할 거리보다 짧아야하므로 
    cnt +=1 # 이동횟수 1 증가
    m_p += k # x에서 y까지에서 총 k만큼 이동하므로 처음 이동거리에서 더해줌
    if cnt % 2 == 0: # cnt가 2의 배수이면
      k += 1 # k는 1증가
  print(cnt)