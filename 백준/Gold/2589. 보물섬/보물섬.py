
from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol))
    visited[srow][scol] = 0

    while queue:
        row, col = queue.popleft()
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < L and 0 <= ncol < W and visited[nrow][ncol] == -1 and grid[nrow][ncol] == 'L':
                visited[nrow][ncol] = visited[row][col] + 1
                queue.append((nrow, ncol))

    # max 찾기
    max_t = 0
    for i in range(L):
        if max_t < max(visited[i]):
            max_t = max(visited[i])

    return max_t


L, W = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(L)]

# 땅인 부분 찾기
lands = deque()
for i in range(L):
    for j in range(W):
        if grid[i][j] == 'L':
            lands.append((i, j))

max_time = 0
for srow, scol in lands:
    visited = [[-1] * W for _ in range(L)]
    time = bfs(srow, scol)
    if max_time < time:
        max_time = time

print(max_time)