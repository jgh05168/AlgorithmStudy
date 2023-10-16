'''
레이저 통신

bfs를 이용하여 위치 탐색
- 만약 현재 direction과 방향이 달라진다면 거울값 + 1
- 경로 저장
'''

import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    min_mirrors = int(1e9)
    pq = []
    heapq.heappush(pq, (-1, srow, scol, -1))
    for temp in range(4):
        visited[temp][srow][scol] = -1
    while pq:
        mirrors, row, col, direction = heapq.heappop(pq)

        if (row, col) == C_list[1]:     # 종료 조건
            min_mirrors = min(min_mirrors, mirrors)
            continue

        if min_mirrors < mirrors:
            continue

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if direction != d:
                new_mirrors = mirrors + 1
            else:
                new_mirrors = mirrors
            if 0 <= nrow < H and 0 <= ncol < W and  grid[nrow][ncol] != '*':
                if visited[d][nrow][ncol] > new_mirrors:
                    visited[d][nrow][ncol] = new_mirrors
                    heapq.heappush(pq, (new_mirrors, nrow, ncol, d))

    return min_mirrors

W, H = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]
visited = [[[int(1e9)] * W for _ in range(H)] for _ in range(4)]

# 초기 C 위치들 구하기
C_list = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'C':
            C_list.append((i, j))

# bfs 시도
min_mirrors = bfs(C_list[0][0], C_list[0][1])

print(min_mirrors)