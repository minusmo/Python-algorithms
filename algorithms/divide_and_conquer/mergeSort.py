def merge_sort(array):
    # step1: divide
    # step2: solve(conquer)
    # step3: combine
    if len(array) <= 4:
        return sorted(array)
    
    left = array[:len(array)//2 + 1]
    right = array[len(array)//2 + 1:]
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return combine(left_sorted, right_sorted)

def combine(left_sorted, right_sorted):
    combined_array = []
    while len(left_sorted) != 0 and len(right_sorted) != 0:
        if left_sorted[0] < right_sorted[0]:
            combined_array.append(left_sorted.pop(0))
        else:
            combined_array.append(right_sorted.pop(0))
    
    combined_array.extend(left_sorted)
    combined_array.extend(right_sorted)
    return combined_array

unsorted_array = [ 2, 4, 5, 234, 1, 8, 7, 99, 43, 42, 22 ]
sorted_array = merge_sort(unsorted_array)
print(sorted_array)