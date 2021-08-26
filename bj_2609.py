n, m = input().split()
n, m = int(n), int(m)
gcd, lcm = 0, 0
for i in range(1,min(n,m)+1):
    if n % i == 0 and m % i == 0:
        gcd = i
for i in range(1, n*m+1):
    if (max(n,m) * i) % min(n,m) == 0:
        lcm = max(n,m) * i
        break
print(gcd, lcm, sep='\n')