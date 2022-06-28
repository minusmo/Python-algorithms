from operator import itemgetter

N, K = [int(i) for i in input().split()]
items = []
for _ in range(N):
    W, V = [int(i) for i in input().split()]
    items.append((W,V))
items = [(0,0)] + sorted(items, key=itemgetter(0))

table = [[0 for _ in range(K+1)] for _ in range(N+1)]

def calculateBestProfit(N, K):
    for i in range(1, N+1):
        for w in range(1, K+1):
            if w - items[i][0] >= 0:
                table[i][w] = max(table[i-1][w], table[i-1][w - items[i][0]] + items[i][1])
            else:
                table[i][w] = table[i-1][w]
            
    return table[N][K]

bestProfit = calculateBestProfit(N, K)
print(bestProfit)