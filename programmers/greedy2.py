def solution(name):
    min_moves = 0
    min_moves = get_moves(name)
    return min_moves

def get_moves(name):
    controls = 0
    move_directions = [0 for _ in range(len(name))]
    
    difference = 0
    for i, char in enumerate(name):
        if char != 'A':
            difference += 1
        right_move, right_index = get_right_move(name, i)
        left_move, left_index = get_left_move(name, i)
        if left_move < right_move:
            move_directions[i] = [-1, left_index]
        else:
            move_directions[i] = [0, right_index]
    
    index = 0
    while difference > 0:
        if name[index] != 'A':
            controls += min_updown_moves(name[index], 'A')
            difference -= 1
        if difference == 0:
            break
        index, moves = change_index(index, move_directions, name)
        controls += moves
    return controls

def get_right_move(name, base_index):
    right_move = 0
    right_index = base_index
    
    for char_index in range(base_index+1, len(name)):
        right_move += 1
        if name[char_index] == 'A':
            continue
        else:
            right_index = char_index
            break
        
    if right_index == base_index:
        for char_index in range(0, base_index):
            right_move += 1
            if name[char_index] == 'A':
                continue
            else:
                right_index = char_index
                break
            
    return [right_move, right_index]

def get_left_move(name, base_index):
    left_move = 0
    left_index = base_index
    for char_index in range(base_index-1, -1, -1):
        left_move += 1
        if name[char_index] == 'A':
            continue
        else:
            left_index = char_index
            break
        
    if left_index == base_index:
        for char_index in range(len(name)-1, base_index, -1):
            left_move += 1
            if name[char_index] == 'A':
                continue
            else:
                left_index = char_index
                break
        
    return [left_move, left_index]


def min_updown_moves(target_char, source_char):
    min_updown_move = 0
    target_order = ord(target_char)
    source_order  = ord(source_char)
    min_updown_move = min(up_moves(target_order, source_order), down_moves(target_order))
    return min_updown_move

def up_moves(target_char, source_char):
    return abs(target_char - source_char)

def down_moves(target_char):
    return abs(ord('Z') - target_char + 1)

def change_index(index, move_directions, name):
    changed_index = move_directions[index][1]
    direction = move_directions[index][0]
    moves = 0
    
    if direction == 0:
        #right
        if changed_index > index:
            moves = changed_index - index
        elif changed_index == index:
            moves = 0
        else:
            moves = len(name) - 1 - index + 1 + changed_index
    else:
        #left
        if changed_index > index:
            moves = index + 1 + len(name) - 1 - changed_index
        elif changed_index == index:
            moves = 0
        else:
            moves = index - changed_index
    return [changed_index, moves]