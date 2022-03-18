from itertools import combinations
def solution(clothes):
    clothes_combinations = 0
    clothes_table = convert_to_table(clothes)
    clothes_combinations = get_combinations(clothes_table)
    return clothes_combinations

def convert_to_table(clothes):
    table = {}
    for name, type in clothes:
        if type in table:
            table[type].append(name)
        else:
            table[type] = [name]
    return table

def get_combinations(clothes_table):
    clothes_combinations = 0
    for number_of_clothes in range(1, len(clothes_table)+1):
        clothes_combinations += combinations_of_clothes(number_of_clothes, clothes_table)
    return clothes_combinations

def combinations_of_clothes(number_of_clothes, clothes_table):
    combinations_with_types = combinations(clothes_table.keys(), number_of_clothes)
    number_of_total_sets = 0
    for types in combinations_with_types:
        number_of_sets = 1
        for type in types:
            number_of_sets *= len(clothes_table[type])
        number_of_total_sets += number_of_sets
    return number_of_total_sets

#이미 계산한 조합을 캐싱해서 이후 조합 연산에 사용할 수 있음.(캐싱)