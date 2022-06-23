# N, M = map(int, input().split())

allCombinations = []

def findCombinations(start, n, m, combination):
    if m == 0:
        addCombination(combination)
        return
    for i in range(start, n+1):
        combination.append(i)
        findCombinations(i+1, n, m-1, combination)
        combination.pop()

def addCombination(combination):
    allCombinations.append(tuple(combination))
    
inputs = [(3,1), (4,2), (4,4)]

for N, M in inputs:
    findCombinations(1, N, M, [])
    for combination in allCombinations:
        print(' '.join([str(i) for i in combination]))
    allCombinations.clear()