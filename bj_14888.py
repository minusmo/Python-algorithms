N = int(input())
numbers = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
operators = sum(operator_list)

min_val = 10**10
max_val = -10**10
def calculate(m, value):
    global min_val, max_val
    if (m > operators):
        min_val = min(value, min_val)
        max_val = max(value, max_val)
    else:
        