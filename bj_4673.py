def dn(n):
    dn = n
    for i in str(n):
        dn += int(i)
    return dn

nums = [0 for _ in range(10001)]

for i in range(1,10001):
    try:
        nums[dn(i)] += 1
    except:
        continue

for n, d_n in enumerate(nums):
    if n == 0:
        continue
    if d_n == 0:
        print(n)