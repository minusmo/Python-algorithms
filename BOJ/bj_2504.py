import sys
from collections import deque
input = sys.stdin.readline

# 1 <= N <= 30
pattern = input().strip('\n')

stack = deque()
val_sum = [0 for _ in range(len(pattern))]

def calculate_val(val_in_between, parenthesis):
    if parenthesis == ')':
        return val_in_between * 2
    else:
        return val_in_between * 3
    
for item in enumerate(pattern):
    if len(stack) == 0:
        stack.append(item)
        val_sum[item[0]] = val_sum[item[0]-1]
    elif (stack[-1][1] == '(' and item[1] == ')') or (stack[-1][1] == '[' and item[1] == ']'):
        if abs(stack[-1][0] - item[0]) == 1:
            val = 0
            if item[1] == ')':
                val = 2
            else:
                val = 3
            val_sum[item[0]] = val_sum[item[0]-1] + val
        else:
            val_in_between = val_sum[item[0]-1] - val_sum[stack[-1][0]]
            calculated_val = calculate_val(val_in_between, item[1])
            val_sum[item[0]] = val_sum[stack[-1][0]] + calculated_val
        stack.pop()
    elif (stack[-1][1] == '(' and item[1] == ']') or (stack[-1][1] == '[' and item[1] == ')'):
        break
    else:
        stack.append(item)
        val_sum[item[0]] = val_sum[item[0]-1]

if len(stack) != 0:
    print(0)
else:
    print(val_sum[-1])