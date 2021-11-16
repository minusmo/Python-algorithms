k, n = map(int,input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

M = max(lines)
m = -1
start = 1
end = M
mid = (start+end)//2
c = sum([line//mid for line in lines])
while start+1 < end:
    if c >= n and mid > m:
        m = mid
        start = mid+1
    else:
        end = mid-1
        
    mid = (start+end)//2
    c = sum([line//mid for line in lines])

if c >= n:
    m = mid

c = sum([line//end for line in lines])
if c >= n:
    m = end

print(m)

# note
# 정수값을 최대값 2^31 -1 까지 배열로 저장하는 것은 메모리 초과를 유발한다. 

# 몇가지 반례
# 4 4
# 10
# 3
# 1
# 1
# :3

# 4 5
# 10 
# 1
# 1
# 1
# :2

# 다른 사람 풀이
# k,n = map(int,input().split())
# A = list()

# for i in range(k):
#     A.append(int(input()))

# s = 1
# e = max(A)
# m = (s+e)//2
# c = sum([q//m for q in A])
# ret = -1

# while s+1 < e:
#     if c>=n:
#         ret = m
#         s = m+1
#     else:
#         e = m-1

#     m = (s+e)//2
#     c = sum([q//m for q in A])

# if c >= n:
#     ret = m

# c = sum([q//e for q in A])
# if c >= n:
#     ret = e

# print(ret)