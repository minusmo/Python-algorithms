N = int(input())

m = 0
def make_one(n, m):
    if n==1:
        return [1,m]
    opers = []
    if n%3==0:
        opers.append(make_one(n//3, m+1))
    if n%2==0:
        opers.append(make_one(n//2, m+1))
    if n-1>0:
        opers.append(make_one(n-1, m+1))
    return min(opers, key=lambda x: x[1])

print(make_one(N,m)[1])

