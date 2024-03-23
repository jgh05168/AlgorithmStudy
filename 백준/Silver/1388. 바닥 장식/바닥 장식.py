'''
풀이 :
for문 탐색하면서 bfs 진행
'-'일 경우에는 col 방향으로만 탐색
'|'일 경우에는 row 방향으로만 탐색 진행
모두 탐색 진행한 후 cnt += 1

'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol, shape):
    queue = deque()
    queue.append((srow, scol))
    visited[srow][scol] = 1

    while queue:
        row, col = queue.popleft()

        if shape == '-':
            for d in range(0, len(dr), 2):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and home[nrow][ncol] == shape:
                    visited[nrow][ncol] = 1
                    queue.append((nrow, ncol))
        else:
            for d in range(1, len(dr), 2):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and home[nrow][ncol] == shape:
                    visited[nrow][ncol] = 1
                    queue.append((nrow, ncol))


n, m = map(int, input().split())
home = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j, home[i][j])
            cnt += 1

print(cnt)