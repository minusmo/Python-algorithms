import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

expression = input().rstrip('\n')

pairs = {}
stack = deque()
for item in enumerate(expression):
    if item[1] == '(':
        pairs[item[0]] = -1
        stack.append(item)
    elif item[1] == ')' and stack[-1][1] == '(':
        pairs[stack[-1][0]] = item[0]
        stack.pop()

results = set()
for i in range(1,len(pairs)+1):
    for combination in combinations(pairs.keys(), i):
        exp = list(expression)
        for position in combination:
            exp[position] = ''
            exp[pairs[position]] = ''
        results.add(''.join(exp))


for result in sorted(results):
    print(result)