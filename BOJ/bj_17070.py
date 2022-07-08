from queue import Queue

N = int(input())
house = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    house.append(row)

moves = {
    "h": [(0,1),(1,1)],
    "v": [(1,0),(1,1)],
    "d": [(0,1),(1,1),(1,0)],
}

def getWays(house, N, moves) -> int:
    ways = 0
    stateQ = Queue()
    initialState = (0,1,"h")
    stateQ.put(initialState)
    while stateQ.qsize() != 0:
        currentState = stateQ.get()
        nextStates = moveState(currentState, moves)
        for nextState in nextStates:
            if isAvailable(nextState, house, N):
                if nextState[0] == N-1 and nextState[1] == N-1:
                    ways += 1
                    continue
                stateQ.put(nextState)
    return ways

def moveState(currentState, moves) -> list:
    nextStates = []
    direction = None
    for move in moves[currentState[2]]:
        if move[0] == 0:
            direction = 'h'
        elif move[1] == 0:
            direction = 'v'
        else:
            direction = 'd'
        nextState = (currentState[0]+move[0], currentState[1]+move[1], direction)
        nextStates.append(nextState)
    return nextStates

def isAvailable(nextState, house, N) -> bool:
    r = nextState[0]
    c = nextState[1]
    direction = nextState[2]
    if r >= N or c >= N:
        return False
    elif house[r][c] == 1:
        return False
    elif direction == 'd':
        if house[r-1][c] == 1 or house[r][c-1] == 1:
            return False
        else:
            return True
    else:
        return True

print(getWays(house, N, moves))