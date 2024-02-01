from collections import deque
import sys

input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

min_v = int(1e9)
n, m = 0, 0
endpoint = (0, 0)


def bfs(maps, srow, scol):
    global min_v

    queue = deque()
    visited = [[[-1] * m for _ in range(n)] for _ in range(2)]
    queue.append((srow, scol, 0))
    visited[0][srow][scol] = 0

    while queue:
        row, col, pull = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and visited[pull][nrow][ncol] == -1 and maps[nrow][ncol] != 'X':
                if pull and maps[nrow][ncol] == 'E':
                    min_v = visited[pull][row][col] + 1
                    return
                if not pull and maps[nrow][ncol] == 'L':
                    queue.append((nrow, ncol, 1))
                    visited[1][nrow][ncol] = visited[pull][row][col] + 1
                else:
                    queue.append((nrow, ncol, pull))
                    visited[pull][nrow][ncol] = visited[pull][row][col] + 1


def solution(maps):
    global min_v, n, m, endpoint

    n, m = len(maps), len(maps[0])
    srow, scol = 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                srow, scol = i, j
            elif maps[i][j] == 'E':
                endpoint = (i, j)

    bfs(maps, srow, scol)

    if min_v == int(1e9):
        answer = -1
    else:
        answer = min_v
    return answer