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
            if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] == -1 and arr[nrow][ncol] != 0:
                if (nrow, ncol) == (srow, scol):
                    continue
                queue.append((nrow, ncol))
                visited[nrow][ncol] = visited[row][col] + 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
srow, scol = 0, 0
find = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            srow, scol = i, j
            find = True
            break
    if find:
        break


visited = [[-1] * M for _ in range(N)]
bfs(i, j)

for i in range(N):
    for j in range(M):
        if visited[i][j] == -1 and not arr[i][j]:
            visited[i][j] = 0

for i in range(N):
    print(*visited[i])