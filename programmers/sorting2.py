from operator import itemgetter

def solution(numbers):
    max_number_to_string = ''
    max_number_in_list = get_max_number_in_list(numbers)
    max_number_to_string = ''.join(max_number_in_list)
    return str(int(max_number_to_string))

def get_max_number_in_list(numbers):
    numbers_in_oneplace_order = sorted(numbers, key=compare_in_place, reverse=True)
    return [str(number) for number in numbers_in_oneplace_order]

def compare_in_place(number):
    return number % 10
    