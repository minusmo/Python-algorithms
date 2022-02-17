def solution(numbers, target):
    ways_to_make_target_number = []
    target_number = target
    visited = [] #queue
    
    def df_search():
        if all_visited(visited, numbers):
            if target_number_can_made(visited, numbers, target_number):
                ways_to_make_target_number.append(1)
            return
        
        for operator in range(2):
            visited.append(operator)
            df_search()
            visited.pop()
    
    df_search()
    return sum(ways_to_make_target_number)

def all_visited(visited, numbers):
    if len(visited) == len(numbers):
        return True
    else:
        return False
    
def target_number_can_made(visited, numbers, target_number):
    reduced_value = 0
    for operator, number in zip(visited, numbers):
        if operator == 0:
            reduced_value += number
        else:
            reduced_value -= number
            
    if reduced_value == target_number:
        return True
    else:
        return False