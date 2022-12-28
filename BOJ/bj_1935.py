import sys
from collections import deque
input = sys.stdin.readline

# N different characters
N = int(input())

expression = input().rstrip('\n')

# A - Z
characters = [chr(i) for i in range(65,91)]
charactersUsed = characters[:N]

# random number for each character
operandVals = []
for _ in range(N):
    operandVals.append(int(input()))

table = dict(zip(charactersUsed,operandVals))

dq = deque()

operators = set(['+','-','*','/'])

def operate(operand1, operand2, exp: str) -> float:
    result = None
    if exp == '+':
        result = float(operand1 + operand2)
    elif exp == '-':
        result = float(operand1 - operand2)
    elif exp == '*':
        result = float(operand1 * operand2)
    else:
        result = float(operand1 / operand2)
    return result

for exp in expression:
    if not exp in operators:
        dq.append(exp)
    else:
        operand2 = dq.pop()
        operand1 = dq.pop()
        if operand2 in charactersUsed:
            operand2 = float(table[operand2])
        if operand1 in charactersUsed:
            operand1 = float(table[operand1])
            
        result = operate(operand1, operand2, exp)
        dq.append(result)
        
print(format(dq.pop(), '.2f'))