N = int(input())

s = [[N,0]]
def makeOne(s):
    n, m = s
    ss = []
    if n%3==0:
        ss.append([n//3, m+1])
    if n%2==0:
        ss.append([n//2, m+1])
    if n-1>1:
        ss.append([n-1, m+1])
    return ss

while N > 1:
    