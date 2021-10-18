from operator import itemgetter
N = int(input())
nums = []
for _ in range(N):
    x, y = input().split()
    x, y = int(x), int(y)
    nums.append((x,y))
nums = sorted(nums,key=itemgetter(1,0))
for x,y in nums:
    print(x,y)