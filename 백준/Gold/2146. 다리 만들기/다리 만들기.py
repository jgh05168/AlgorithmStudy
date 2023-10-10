from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def init():
    # 땅 값만 저장
    lands = []
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                lands.append((i, j))

    # 땅 별로 색 나누기
    new_map = [[0] * N for _ in range(N)]
    idx = 1
    for row, col in lands:
        if not new_map[row][col]:
            queue = deque()
            queue.append((row, col))
            new_map[row][col] = idx
            while queue:
                row, col = queue.popleft()

                for d in range(len(dr)):
                    nrow, ncol = row + dr[d], col + dc[d]
                    if 0 <= nrow < N and 0 <= ncol < N and not new_map[nrow][ncol] and grid[nrow][ncol]:
                        new_map[nrow][ncol] = idx
                        queue.append((nrow, ncol))
            idx += 1

    return new_map, lands, idx

def bfs(srow, scol, land):
    global min_v
    queue = deque()
    queue.append((srow, scol, 0))
    visited = [[-1] * N for _ in range(N)]
    visited[srow][scol] = 0

    while queue:
        row, col, loc = queue.popleft()

        if min_v <= loc:
            continue

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and visited[nrow][ncol] == -1 and new_map[nrow][ncol] != land:
                if new_map[nrow][ncol] > 0:
                    min_v = min(min_v, visited[row][col])
                    return
                visited[nrow][ncol] = visited[row][col] + 1
                queue.append((nrow, ncol, loc + 1))


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

new_map, lands, islands = init()      # 초기 설정

min_v = N * N

for row, col in lands:
    # 바다랑 인접한 곳이 하나라도 존재하는지 확인
    adj_ocean = False
    for d in range(len(dr)):
        nrow, ncol = row + dr[d], col + dc[d]
        if 0 <= nrow < N and 0 <= ncol < N and not new_map[nrow][ncol]:
            adj_ocean = True
            break

    # bfs 탐색
    if adj_ocean:
        bfs(row, col, new_map[row][col])

print(min_v)