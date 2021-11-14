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
        index = index+k-1
        while index >= len(cll):
            index -= len(cll)
        y_perm.append(cll.pop(index))
print('<', end='')
for i in range(n):
    if i == n-1:
        print(y_perm[i], '>', sep='')
    else:
        print(y_perm[i], end=', ')
