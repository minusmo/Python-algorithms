from queue import Queue
t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    importances = map(int, input().split())
    sq = Queue()
    for ind, imp in enumerate(importances):
        sq.put((1 if ind == M else 0, imp))
    turn = 0
    while not sq.empty():
        doc = sq.get()
        if len(list(filter(lambda x: x[1]>doc[1],sq.queue))) > 0:
            sq.put(doc)
        else:
            turn += 1
            if doc[0] == 1:
                print(turn)
                break