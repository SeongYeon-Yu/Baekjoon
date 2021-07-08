s = input()
al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in al:
  s = s.replace(i, 'a')
print(len(s))