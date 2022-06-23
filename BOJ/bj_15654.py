# N, M = map(int, input().split())
# items = list(map(int, input().split()))
# items = sorted(items)

allPermutations = []

def findPermutations(start, n, m, permutation, items, items_selected):
    if m == 0:
        addPermutation(permutation)
        return
    for i in range(start, n):
        if items_selected[i] == 1:
            continue
        permutation.append(items[i])
        items_selected[i] = 1
        findPermutations(start, n, m-1, permutation, items, items_selected)
        permutation.pop()
        items_selected[i] = 0

def addPermutation(permutation):
    allPermutations.append(tuple(permutation))

inputs = [(3,1, [2, 4, 5]), (4,2, [1, 7, 8, 9])]

for N, M, items in inputs:
    items_selected = [0 for _ in range(N)]
    findPermutations(0, N, M, [], items, items_selected)
    for permutation in allPermutations:
        print(' '.join([str(i) for i in permutation]))
    allPermutations.clear()