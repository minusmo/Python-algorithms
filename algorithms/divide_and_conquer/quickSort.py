
def quick_sort(not_sorted):
    # step1: divide
    # step2: conquer
    # step3: combine --> optional!!!
    
    if len(not_sorted) <= 4:
        return sorted(not_sorted)
    
    pivot_index = 0
    left = []
    right = []
    
    for number in not_sorted:
        if number < not_sorted[pivot_index]:
            left.append(number)
        elif number > not_sorted[pivot_index]:
            right.append(number)
    
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    
    return left_sorted + [not_sorted[pivot_index]] + right_sorted

unsorted_array = [ 2, 4, 5, 234, 1, 8, 7, 99, 43, 42, 22 ]
sorted_array = quick_sort(unsorted_array)
print(sorted_array)