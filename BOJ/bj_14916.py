import sys
input = sys.stdin.readline

n = int(input())

twos = 0
fives = 0

can_exchange = False
fives = n // 5
twos = (n - fives*5) // 2
while not can_exchange:
  if fives == 0 and twos * 2 != n:
    break
  if fives * 5 + twos * 2 == n:
    can_exchange = True
    break
  else:
    fives -= 1
    twos = (n-fives*5) // 2

if n - fives*5 - twos*2 != 0:
  print(-1)
else:
  print(twos + fives)