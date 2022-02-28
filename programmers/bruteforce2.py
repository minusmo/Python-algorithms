from math import sqrt, ceil

def solution(numbers):
    prime_numbers = 0
    prime_numbers = get_prime_numbers(numbers)
    return prime_numbers

def get_prime_numbers(numbers):
    prime_numbers = [0] * (10**7)
    numbers_to_check = []
    checked_indexes = []
    
    def dfs_check(numbers_to_check):
        if len(numbers_to_check) > 0:
            if is_prime_number(numbers_to_check):
                prime_number = int(''.join(numbers_to_check))
                prime_numbers[prime_number] = 1
        for i in range(len(numbers)):
            if i in checked_indexes:
                continue
            numbers_to_check.append(numbers[i])
            checked_indexes.append(i)
            dfs_check(numbers_to_check)
            numbers_to_check.pop()
            checked_indexes.pop()
            
    def is_prime_number(numbers_to_check):
        is_prime = False
        number_in_string  = ''.join(numbers_to_check)
        number_to_check = int(number_in_string)
        is_prime = check_prime(number_to_check)
        return is_prime
    
    def check_prime(number_to_check):
        if number_to_check <= 1:
            return False
        elif number_to_check < 4:
            return True
        
        for i in range(2, ceil(sqrt(number_to_check))+1):
            if number_to_check % i == 0:
                return False
        return True
    
    dfs_check(numbers_to_check)
    return sum(prime_numbers)