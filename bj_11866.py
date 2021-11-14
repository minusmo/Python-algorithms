from collections import deque

n, k = input().split()
n, k = int(n), int(k)
cll = [i+1 for i in range(n)]
index = 0
y_perm = []
while len(cll) != 0:
    try:
        y_perm.append(cll.pop(index+k-1))
        index = index+k-1
    except:
        y_perm.append(cll.pop(-(index+k-1)+len(cll)+k-1))
        index = -(index+k-1)+len(cll)+k-1
print('<', ', '.join(y_perm), '>', sep='')
