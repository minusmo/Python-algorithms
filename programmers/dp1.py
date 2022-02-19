from readline import parse_and_bind


def solution(N, number):
    min_N_usage = 9
    
    min_N_usage = get_min_N_usage(N, number)
    if min_N_usage > 8:
        return -1
    return min_N_usage

def get_min_N_usage(N, number):
    N_usage = [0] * (number+1)

    for target_number in range(1, number+1):
        N_usage[target_number] = number_i_of_N_used(N, target_number, N_usage)
    
    return N_usage[number]

def number_i_of_N_used(N, target_number, N_usage):
    if target_number < N:
        return lower_N(target_number)
    elif target_number == N:
        return 1
    else:
        return greater_N(target_number, N, N_usage)
    
def lower_N(target_number):
    return target_number + 1

def greater_N(target_number, N, N_usage):
    
    return min(using_sum, using_product, using_serize)