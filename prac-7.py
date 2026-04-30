# Implement 8 puzzle problem using A star Algorithm.

from collections import deque

goal = [[1,2,3],[4,5,6],[7,8,0]]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state, x, y, dx, dy):
    new = [row[:] for row in state]
    nx, ny = x+dx, y+dy
    if 0 <= nx < 3 and 0 <= ny < 3:
        new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
        return new
    return None

def bfs(start):
    q = deque([(start, [])])   # store path also
    visited = []

    while q:
        curr, path = q.popleft()

        # print current state
        print("Current State:")
        for row in curr:
            print(row)
        print()

        if curr == goal:
            print("Goal State Reached!")
            return

        visited.append(curr)

        x, y = find_zero(curr)

        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx, dy in moves:
            new_state = move(curr, x, y, dx, dy)
            if new_state and new_state not in visited:
                q.append((new_state, path + [curr]))

    print("No Solution")


start = [[1,2,3],[4,0,6],[7,5,8]]
bfs(start)