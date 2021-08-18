n, m = input().split()
n, m = int(n), int(m)

board = []

for _ in range(n):
    row = input()
    board.append(list(row))
    
mini = 1000000

def checkboard(board):
    wturns = 0
    bturns = 0
    
    cell = 'W'
    for row in board:
        for char in row:
            if char != cell:
                wturns += 1
            cell = 'B' if cell == 'W' else 'W'
        cell = 'B' if cell == 'W' else 'W'
        
    cell = 'B'
    for row in board:
        for char in row:
            if char != cell:
                bturns += 1
            cell = 'W' if cell == 'B' else 'B'
        cell = 'W' if cell == 'B' else 'B'
    return min(wturns, bturns)

for i in range(n-7):
    for j in range(m-7):
        chessboard = board[i:i+8]
        for l in range(len(chessboard)):
            chessboard[l] = chessboard[l][j:j+8]
        turns = checkboard(chessboard)
        mini = turns if turns < mini else mini
        
print(mini)
