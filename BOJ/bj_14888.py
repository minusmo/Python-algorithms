N = int(input())
numbers = [None]+list(map(int, input().split()))
operator_list = [None]+list(map(int, input().split()))
order = [-1]*N
min_val = 10**10
max_val = -10**10

def compute(order):
    value = numbers[1]
    for i in range(1, N):
        if order[i] == 1:
            value += numbers[i+1]
        if order[i] == 2:
            value -= numbers[i+1]
        if order[i] == 3:
            value *= numbers[i+1]
        if order[i] == 4:
            if value < 0:
                new_value = -(-value//numbers[i+1])
                value = new_value
            else:
                new_value = value // numbers[i+1]
                value = new_value
    return value
    
def calculate(m):
    global min_val, max_val
    if (m > N-1):
        value = compute(order)
        min_val = min(value, min_val)
        max_val = max(value, max_val)
    else:
        for i in range(1, 5):
            if operator_list[i] >= 1:
                # 연산자 사용가능
                operator_list[i] -= 1
                order[m] = i
                calculate(m+1)
                operator_list[i] += 1
                order[m] = -1
            else:
                # 연산자 사용불가능
                pass
            
            
calculate(1)
print(max_val)
print(min_val)