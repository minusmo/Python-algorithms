import sys
input = sys.stdin.readline

N = int(input())
n1,n2,n3,n = 0,1,1,2

while n <= N:
  n += 1
  n3 = n1+n2
  n1 = n2
  n2 = n3

if N == 0:
  print(n1)
else:
  print(n3)