'''
만약 도착지의 위치가 x라면 갈 수 있음.
아니라면 갈 수 없음(queue 저장 x)
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol))
    visited[srow][scol] += 1

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m:
                # 만약 도착지점이 뚫려있다면
                if visited[nrow][ncol] == 1:
                    if (nrow, ncol) == (erow - 1, ecol - 1):
                        return True
                    else: continue
                if frozen[nrow][ncol] == 'X':
                    if (nrow, ncol) == (erow - 1, ecol - 1):
                        return True
                    else: continue
                visited[nrow][ncol] = 1
                queue.append((nrow, ncol))

    return False


n, m = map(int, input().split())
frozen = [list(input().rstrip()) for _ in range(n)]
srow, scol = map(int, input().split())
erow, ecol = map(int, input().split())
visited = [[0] * m for _ in range(n)]
ans = False

for i in range(n):
    for j in range(m):
        if frozen[i][j] == 'X':
            visited[i][j] = 1

ans = bfs(srow - 1, scol - 1)
if ans:
    print("YES")
else:
    print('NO')