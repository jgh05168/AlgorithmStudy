'''
bfs
벽은 10개까지 부술 수 있다.

visited 배열을 3차원으로 생성. 10 by 1000 by 1000

10 * 1000 * 1000 < 20000000
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol, scrash):
    queue = deque()
    queue.append((srow, scol, scrash))
    visited[scrash][srow][scol] = 1

    while queue:
        row, col, crash = queue.popleft()

        if crash > K:      # 최대 부술 수 있는 횟수 count
            continue

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not visited[crash][nrow][ncol]:
                if (nrow, ncol) == (N - 1, M - 1):       # 정점에 도달한 경우
                    # 만약 벽 부수는 횟수가 10번 미만 or 10번 다 부쉈고, 벽에 막혀있지 않다면
                    if crash < K or (not maze[nrow][ncol] and crash == K):
                        return visited[crash][row][col] + 1

                if not maze[nrow][ncol]:
                    visited[crash][nrow][ncol] = visited[crash][row][col] + 1
                    queue.append((nrow, ncol, crash))
                else:
                    if crash < K and not visited[crash + 1][nrow][ncol]:    # 벽을 뚫고간 부분이 존재하지 않아야 갈 수 있다.
                        visited[crash + 1][nrow][ncol] = visited[crash][row][col] + 1
                        queue.append((nrow, ncol, crash + 1))

    return -1


N, M, K = map(int, input().split())
visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
maze = [list(map(int, input().rstrip())) for _ in range(N)]

if N == 1 and M == 1:
    print(1)
else:
    ans = bfs(0, 0, 0)

    print(ans)