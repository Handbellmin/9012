import sys

input = sys.stdin.readline
n = int(input())
chk_ls = []
for i in range(n):
  str = input()
  n = 0
  chk = True
  for k in str:
    if k == '(':
      n += 1
    elif k == ')':
      n -= 1
    if n < 0:
      chk = False
      break
  if chk == True and n == 0:
    chk_ls.append('YES')
  else:
    chk_ls.append('NO')
  
for chk in chk_ls:
  print(chk)
