'''
벽은 꼭 3개를 세워야 한다. -> 64C3
일부 칸은 바이러스가 존재한다.
    바이러스는 상하좌우로 이동한다.

안전구역의 최대 넓이를 구하자

완탐 + bfs

벽을 3군데에 세워본 뒤 bfs를 수행하고 남는 공간의 최대값을 업데이트
-> 순열을 사용해서 진행해보자

'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(start_safety_zones):
    global max_safety_zones
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    for v in range(len(virus)):
        queue.append(virus[v])
        visited[virus[v][0]][virus[v][1]] = 1
    safety_zone_cnt = start_safety_zones

    while queue:
        row, col = queue.popleft()
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not visited[nrow][ncol] and not center[nrow][ncol]:
                visited[nrow][ncol] = 1
                queue.append((nrow, ncol))
                safety_zone_cnt -= 1

    max_safety_zones = max(max_safety_zones, safety_zone_cnt)


def permutation(build, next, safety_cnt):
    # 벽을 모두 세웠다면, 바이러스를 퍼트려보기
    if build == 3:
        bfs(safety_cnt)
        return

    if next >= len(safety_zones):
        return
    for j in range(next, len(safety_zones)):
        if not selected[j]:
            center[safety_zones[j][0]][safety_zones[j][1]] = 1      # 벽 세우기
            selected[j] = 1
            permutation(build + 1, j + 1, safety_cnt - 1)
            center[safety_zones[j][0]][safety_zones[j][1]] = 0      # 벽 허물기
            selected[j] = 0


N, M = map(int, input().split())
center = [list(map(int, input().split())) for _ in range(N)]

virus = []
safety_zones = []
for i in range(N):
    for j in range(M):
        if center[i][j] == 2:
            virus.append((i, j))
        elif not center[i][j]:
            safety_zones.append((i, j))

max_safety_zones = 0
# 3군데에 벽 놔보기
selected = [0] * len(safety_zones)
permutation(0, 0, len(safety_zones))


print(max_safety_zones)