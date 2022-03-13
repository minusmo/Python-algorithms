triangle = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,2,3,4,0],
    [5,6,7,8,9],
    [0,0,0,0,0]
]

def solution(triangle, size):
    rotated_triangle = [[] for _ in range(size)]
    rotated_triangle = rotate_triangle_60(triangle, rotated_triangle, size)
    return rotated_triangle

def rotate_triangle_60(triangle, rotated_triangle, size):
    triangle_graph = get_adjacent_list(triangle, size)
    root_node = right_leaf_node(triangle, size)
    bf_search(root_node, rotated_triangle)
    return rotated_triangle

def get_adjacent_list(triangle, size):
    adjacent_list = {}
    possible_nodes = [[-1,0], [0,1], [1,0], [0,-1]]
    start_vertex = [1, size//2]
    vertex_to_visit = []
    vertex_to_visit.append(start_vertex)
    
    while len(vertex_to_visit) > 0:
        current_vertex = vertex_to_visit.pop(0)
        x = current_vertex[0]
        y = current_vertex[1]
        
        for possible_node in possible_nodes:
            if is_adjacent_node(x, y, possible_node):
                adjacent_node = [x+possible_node[0], y+possible_node[1]]
                vertex_to_visit.append(adjacent_node)
                adjacent_list[triangle[x,y]] = update_adjacent_list(adjacent_list[triangle[x,y]], adjacent_node)
    
            
def right_leaf_node(triangle, size):
    return triangle[size-1][size-1]