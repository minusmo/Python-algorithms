N, M = map(int, input().split())
pokedex = {}
pokedex_by_index = {}
for i in range(N):
    name = input()
    pokedex[name] = i+1
    pokedex_by_index[i+1] = name
for _ in range(M):
    q = input()
    try:
        q = int(q)
        print(pokedex_by_index[q])
    except:
        print(pokedex[q])