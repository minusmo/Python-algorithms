def intTriangle():
    N = int(input())
    numbers_in_triangle = [[-1]]
    max_sum_at_each_number = [[-1]]
    for _ in range(N):
        numbers_in_each_level = get_numbers_in_each_level()
        numbers_in_triangle.append(numbers_in_each_level)
        max_sum_at_each_number.append([0]*len(numbers_in_each_level))
    
    for row in range(1, N+1):
        for i in range(row):
            if has_no_parent_right(row, i):
                max_sum_at_each_number[row][i] = max_sum_at_each_number[row-1][i] + numbers_in_triangle[row][i]
            elif has_no_parent_both(row, i):
                max_sum_at_each_number[row][i] = 
            else:
                max_sum_at_each_number[row][i] = bigger_sum_in_two_route(max_sum_at_each_number[row-1][i], max_sum_at_each_number[row-1][i+1]) + numbers_in_triangle[row][i]
    return max(max_sum_at_each_number[N])

def get_numbers_in_each_level():
    return list(map(int, input().split()))

def bigger_sum_in_two_route(parent_left, parent_right):
    return max(parent_left, parent_right)