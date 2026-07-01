from collections import deque
from typing import List


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# Possible bug: cells get added to the queue multiple times before they're 
# marked visited, since visited.add() happens when a cell is popped, not 
# when it's enqueued. So if two different cells both point to the same neighbor 
# before that neighbor is processed, it gets queued twice — leading to duplicate 
# entries in res and wasted work (worse on large/dense grids).
def runBFS(board: List[List[str]], start) -> None:
    visited = set()
    res = []

    q = deque([(start[0], start[1])])
    visited.add((start[0], start[1]))

    while q:
        x, y = q.popleft()
        res.append(board[x][y])

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited:
                continue
            if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]):
                visited.add((nx, ny))
                q.append((nx, ny))

    print(res)


def runDFS(board: List[List[str]], start) -> None:
    visited = set()
    res = []

    def dfs(x, y):
        visited.add((x, y))
        res.append(board[x][y])

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited:
                continue
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                dfs(nx, ny)

    dfs(start[0], start[1])
    print(res)


if __name__ == "__main__":
    board = [
        ["A","B","C","D"],
        ["E","F","G","H"],
        ["I","J","K","L"]
    ]

    print("Iteratively run bfs:")
    runBFS(board, (0, 0))

    print("Recursively run dfs:")
    runDFS(board, (0, 0))