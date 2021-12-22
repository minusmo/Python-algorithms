N = int(input())
numbers = [None]+list(map(int, input().split()))
operator_list = [None]+list(map(int, input().split()))
order = [-1]*N
min_val = 10**10
max_val = -10**10

def compute(operand1, operator, opearand2):
    if operator == 1:
        return operand1 + opearand2
    if operator == 2:
        return operand1 - opearand2
    if operator == 3:
        return operand1 * opearand2
    if operator == 4:
        if operand1 < 0:
            return -(-operand1//opearand2)
        else:
            return operand1 // opearand2
    
def calculate(m, value):
    global min_val, max_val
    if (m > N-1):
        min_val = min(value, min_val)
        max_val = max(value, max_val)
    else:
        for i in range(1, 5):
            if operator_list[i] >= 1:
                # 연산자 사용가능
                operator_list[i] -= 1
                order[m] = i
                new_value = compute(value, i, numbers[m+1])
                calculate(m+1, new_value)
                operator_list[i] += 1
                order[m] = -1
            else:
                # 연산자 사용불가능
                pass
            
            
calculate(1, numbers[1])
print(max_val)
print(min_val)