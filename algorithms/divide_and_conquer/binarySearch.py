sorted_array = [1, 2, 4, 5, 7, 8, 22, 42, 43, 99, 234]

def binary_search(sorted_array, target_number, low, high):
    # step1: divide
    # step2: solve(conquer)
    # step3: combine --> optional!!!
    
    if high - low <= 4:
        try:
            return sorted_array.index(target_number, low, high)
        except:
            return -1
    
    med = (low + high) // 2
    target_index = -1
    
    if low < high:
        if sorted_array[med] == target_number:
            target_index = med
        elif sorted_array[med] < target_number:
            target_index = binary_search(sorted_array, target_number, med+1, high)
        else:
            target_index = binary_search(sorted_array, target_number, low, med+1)
    return target_index

print(binary_search(sorted_array, 99, 0, len(sorted_array)))
print(binary_search(sorted_array, 200, 0, len(sorted_array)))