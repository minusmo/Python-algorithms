import sys
input = sys.stdin.readline

S = int(input())

def getN(s):
  n = 1
  while not (n*n+n) > 2*s:
    n += 1
  n -= 1
  return n

print(getN(S))