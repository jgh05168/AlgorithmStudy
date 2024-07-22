'''
도마도

하루가 지나면 익은 토마토들 인접한 곳에 있지 않은 익지 않은 도마도들은 익는다.

상하좌우위아래 탐색해야한다.

1. 토마토 위치를 먼저 파악
2. 위치를 기반으로 상하좌우위아래 탐색
- 모두 익지 못하는 상황이면 -1 출력
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1, 0, 0]
dc = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def bfs(tomatoes):
    queue = deque(tomatoes)

    while queue:
        h, r, c = queue.popleft()

        for d in range(len(dr)):
            nh, nr, nc = h + dh[d], r + dr[d], c + dc[d]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and visited[nh][nr][nc] == -1:
                # 익지 않은 토마토라면 queue에 저장
                if not grid[nh][nr][nc]:
                    queue.append((nh, nr, nc))
                    visited[nh][nr][nc] = visited[h][r][c] + 1


M, N, H = map(int, input().split())
grid = []
for _ in range(H):
    grid.append([list(map(int, input().split())) for _ in range(N)])
visited = [[[-1] * M for _ in range(N)] for _ in range(H)]

tomatoes = []       # 높이, 행, 열
# 익은 토마토 위치부터 찾기
for i in range(H):
    for j in range(N):
        for k in range(M):
            if grid[i][j][k] == 1:
                tomatoes.append((i, j, k))
                visited[i][j][k] = 0

bfs(tomatoes)

# bfs 탐색이 끝난 뒤 토마토가 모두 숙성되었는지 체크
# 100 x 100 x 100
ans = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 만약 익지 않은 토마토가 존재한다면, -1 출력 후 종료
            if visited[i][j][k] == - 1 and not grid[i][j][k]:
                print(-1)
                exit()
            elif not grid[i][j][k]:
                ans = max(ans, visited[i][j][k])

print(ans)
