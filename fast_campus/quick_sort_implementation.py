def quick_sort(not_sorted):
    if len(not_sorted) <= 1:
        return not_sorted
    
    quick_sorted = []
    pivot = len(not_sorted) // 2
    lower_than_pivot = []
    higher_than_pivot = []
    for compared in not_sorted:
        if compared < not_sorted[pivot]:
            lower_than_pivot.append(compared)
        elif compared > not_sorted[pivot]:
            higher_than_pivot.append(compared)
            
    quick_sorted.extend(quick_sort(lower_than_pivot))
    quick_sorted.append(not_sorted[pivot])
    quick_sorted.extend(quick_sort(higher_than_pivot))
    return quick_sorted

not_sorted = [3,4,1,10,11,92,37,29,94,478,28,35,67]
quick_sorted = quick_sort(not_sorted)
print(quick_sorted)