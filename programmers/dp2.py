def solution(triangle):
    max_path_sum = 0
    max_path_sum = max(get_path_sums(triangle))
    return max_path_sum

def get_path_sums(triangle):
    path_sums = [[0]*i for i in range(1, len(triangle)+1)]
    path_sums[0] = triangle[0]
    for row in range(2, len(triangle)+1):
        current_row = row - 1
        for i, node in enumerate(triangle[current_row]):
            previous_row = row - 2
            path_sums[current_row][i] = max(left_parent_node_sum(path_sums[previous_row], i), right_parent_node_sum(path_sums[previous_row], i, previous_row)) + node
            
    return path_sums[-1]

def left_parent_node_sum(previous_path_sums, i):
    current_node = i
    if current_node == 0:
        return 0
    else:
        return previous_path_sums[current_node-1]

def right_parent_node_sum(previous_path_sums, i, previous_row):
    current_node = i
    if current_node == previous_row + 1:
        return 0
    else:
        return previous_path_sums[current_node]