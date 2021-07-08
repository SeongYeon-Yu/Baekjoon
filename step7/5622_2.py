al = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
cnt = 0
for i in range(len(s)):
  for j in al:
    if j in al:
      if s[i] in j:
        cnt += al.index(j) + 3
print(cnt)