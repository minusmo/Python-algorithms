def solution(number, k):
    largest_number = ''
    largest_number = get_largest_number(number, k)
    return largest_number

def get_largest_number(number, k):
    number = list(number)
    max_number = []
    numbers_need = len(number) - k
    left_bound_index = 0
    right_bound_index = len(number) - numbers_need + 1
    for i in range(numbers_need):
        max_number_precede, max_number_index = find_max_number_precede(number, left_bound_index, right_bound_index)
        left_bound_index = max_number_index + 1
        right_bound_index += 1
        number[max_number_index] = -1
        max_number.append(max_number_precede)
    return ''.join([str(digit) for digit in max_number])

def find_max_number_precede(number, left_bound_index, right_bound_index):
    max_number_index = 0
    max_number = -1
    for i in range(left_bound_index, right_bound_index):
        if int(number[i]) > max_number:
            max_number = int(number[i])
            max_number_index = i
    return [max_number, max_number_index]