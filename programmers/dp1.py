from enum import Enum

def solution(N, number):
    N_used = -1
    N_used = get_min_N_used(N, number)
    return N_used

def get_min_N_used(N, number):
    N_used = -1
    Ns = [[] for _ in range(9)]
    Ns[1] = [N]
    for operator in Operator:
        result = calculate(N, N, operator)
        Ns[2].append(result)
    Ns[2].append(N * int('1' * 2))
    
    if number in Ns[1]:
        return 1
    elif number in Ns[2]:
        return 2
    
    for number_of_N_used in range(3, 9):
        Ns[number_of_N_used] = numbers_using_N(Ns, number_of_N_used, N)
        if number in Ns[number_of_N_used]:
            return number_of_N_used
    return N_used

class Operator(Enum):
    PLUS = 0
    Minus = 1
    Multiply = 2
    Divide = 3

def numbers_using_N(Ns, number_of_N_used, N):
    numbers_with_N = []
    for n in range(1, number_of_N_used):
        numbers_with_N.extend(numbers_with_less_N(Ns[n], Ns[number_of_N_used - n]))
    
    numbers_with_N.append(N * int('1' * number_of_N_used))
    return numbers_with_N

def numbers_with_less_N(left_operands, right_operands):
    numbers_with_N_sub = []
    for left_operand in left_operands:
        for right_operand in right_operands:
            for operator in Operator:
                result = calculate(left_operand, right_operand, operator)
                if result != None:
                    numbers_with_N_sub.append(result)
    return numbers_with_N_sub

def calculate(left_operand, right_operand, operator):
    if operator == Operator.PLUS:
        return left_operand + right_operand
    elif operator == Operator.Minus:
        return left_operand - right_operand
    elif operator == Operator.Multiply:
        return left_operand * right_operand
    else:
        try:
            return left_operand // right_operand
        except:
            return 0