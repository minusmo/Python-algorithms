import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int, input().split())
is_sol_found = False
for x in range(-999,1000):
  for y in range(-999,1000):
    if (a*x + b*y == c) and (d*x+e*y == f):
      print(x,y,sep=' ')
      is_sol_found = True
      break
  if is_sol_found:
    break