'''
석유시추

섬 넘버를 저장
석유 발견 시 bfs 돌리기. -> set으로 col 저장
set에 저장된 col에 석유 수량 더해주기

'''

from collections import deque
import sys

input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
oil_dict = {}


def bfs(srow, scol, visited, land, n, m):
    queue = deque()
    queue.append((srow, scol))
    col_set = set()
    visited[srow][scol] = 1
    col_set.add(scol)
    oil_cnt = 0
    while queue:
        row, col = queue.popleft()
        oil_cnt += 1

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and land[nrow][ncol]:
                col_set.add(ncol)
                queue.append((nrow, ncol))
                visited[nrow][ncol] = 1

    for ccol in col_set:
        oil_dict[ccol] += oil_cnt


def solution(land):
    n = len(land)
    m = len(land[0])

    visited = [[0] * m for _ in range(n)]

    # 열 딕셔너리 초기화
    for i in range(m):
        oil_dict.update({i: 0})

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                bfs(i, j, visited, land, n, m)

    max_v = 0
    for col_num, oil_cnt in oil_dict.items():
        if max_v < oil_cnt:
            max_v = oil_cnt

    return max_v
