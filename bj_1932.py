def intTriangle():
    N = int(input())
    numbers_in_triangle = [-1]
    max_sum_at_each_number = [0]
    for _ in range(N):
        numbers_in_each_level = get_numbers_in_each_level()
        numbers_in_triangle.extend(numbers_in_each_level)
        max_sum_at_each_number.extend([0]*len(numbers_in_each_level))
        
    numbers = len(numbers_in_triangle)
    for row in range(1, numbers+1):
        if has_no_parent_left(row, i):
            max_sum_at_each_number[row][i] = max_sum_at_each_number[row-1][i] + numbers_in_triangle[row][i]
        elif has_no_parent_right(row, i):
            max_sum_at_each_number[row][i] = 
        else:
            max_sum_at_each_number[row][i] = bigger_sum_in_two_route(max_sum_at_each_number[row-1][i], max_sum_at_each_number[row-1][i+1]) + numbers_in_triangle[row][i]
    return max(max_sum_at_each_number[N])

def get_numbers_in_each_level():
    return list(map(int, input().split()))

def bigger_sum_in_two_route(parent_left, parent_right):
    return max(parent_left, parent_right)


MAX_SUM_OF_ROUTE_IN_TRIANGLE = 30
def test_case_of_5():
    assert intTriangle() == MAX_SUM_OF_ROUTE_IN_TRIANGLE
    
"""
5

7 / 1
3 8 / 2
8 1 0 / 3
2 7 4 4 / 4
4 5 2 6 5 / 5
"""