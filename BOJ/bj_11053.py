N = int(input())
items = list(map(int, input().split()))

def getLongestSubSequence(items):
    longestSubSequence = [1] * N
    maxLen = 0
    for i in range(1, N):
        for j in range(i):
            if items[i] > items[j] and longestSubSequence[i] < longestSubSequence[j] + 1:
                longestSubSequence[i] = longestSubSequence[j] + 1
    for i in range(N):
        maxLen = max(maxLen, longestSubSequence[i])
        
    return maxLen

print(getLongestSubSequence(items))