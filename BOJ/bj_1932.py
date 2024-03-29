def intTriangle():
    N = int(input())
    numbers_in_triangle = [0]
    max_sum_at_each_number = [0]
    for _ in range(N):
        numbers_in_each_level = get_numbers_in_each_level()
        numbers_in_triangle.extend(numbers_in_each_level)
        max_sum_at_each_number.extend([0]*len(numbers_in_each_level))
        
    numbers = len(numbers_in_triangle)
    passed_numbers = 1
    max_sum_at_each_number[1] = numbers_in_triangle[1]
    for currentLevel in range(2, N+1):
        prevLevel = currentLevel - 1
        for i in range(passed_numbers+1, passed_numbers+currentLevel+1):
            if i == passed_numbers+1:
                max_sum_at_each_number[i] = numbers_in_triangle[i] + max_sum_at_each_number[i-prevLevel]
            elif i == passed_numbers+currentLevel:
                max_sum_at_each_number[i] = numbers_in_triangle[i] + max_sum_at_each_number[i-currentLevel]
            else:
                max_sum_at_each_number[i] = numbers_in_triangle[i] + max_between_prev_route(max_sum_at_each_number[i-currentLevel], max_sum_at_each_number[i-prevLevel])
        passed_numbers += currentLevel
    return max(max_sum_at_each_number[-N:])

def get_numbers_in_each_level():
    return list(map(int, input().split()))

def max_between_prev_route(parent_left, parent_right):
    return max(parent_left, parent_right)

print(intTriangle())

"""
5

7 / 1
3 8 / 2
8 1 0 / 3
2 7 4 4 / 4
4 5 2 6 5 / 5
"""