import sys
from collections import defaultdict

input = sys.stdin.readline

species = defaultdict(int)

total = 0
while True:
    breed = input()
    if not breed:
        break
    else:
        species[breed.rstrip('\n')] += 1
        total += 1
        
species = sorted(species.items(), key= lambda x : (x[0], x[1]))

for item, count in species:
    ratio = count/total
    print(item, format(ratio*100, '.4f'), sep=' ')