from operator import itemgetter
N = int(input())
nums = []
for _ in range(N):
    x, y = input().split()
    x, y = int(x), int(y)
    nums.append((x,y))
nums = sorted(nums,key=itemgetter(0,1))
for x,y in nums:
    print(x,y)