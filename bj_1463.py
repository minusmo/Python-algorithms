N = int(input())

# m = 0
# def make_one(n, m):
#     if n==1:
#         return [1,m]
#     opers = []
#     if n%3==0:
#         opers.append(make_one(n//3, m+1))
#     if n%2==0:
#         opers.append(make_one(n//2, m+1))
#     if n-1>0:
#         opers.append(make_one(n-1, m+1))
#     return min(opers, key=lambda x: x[1])

# def make_one(n):
#     dp = [0 for _ in range(n+1)]
#     if n<=1:
#         return 0
#     if dp[n]==0:
#         dp[n] = min(make_one(n//3), make_one(n//2), make_one(n-1))+1
#     return dp[n]

def make_one(n):
    if n==1:
        return 0
    if n==2 or n==3:
        return 1
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    if n > 3:
        for i in range(4,n+1):
            op_three = dp[i//3] if i%3==0 else 1000000
            op_two = dp[i//2] if i%2==0 else 1000000
            op_one = dp[i-1] if i-1>0 else 1000000
            dp[i] = min(op_three, op_two, op_one)+1
    return dp[n]

print(make_one(N))