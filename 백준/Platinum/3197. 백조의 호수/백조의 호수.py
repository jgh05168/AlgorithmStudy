'''
백조의 호수

- 땅과 바다 리스트 2개를 받는다.
- 바다에 대해서는 union-find 실행

'.'으로 바뀔 수 있는 위치를 토대로 만약 '.'이 2 개 이상 존재하고, 서로 다른 바다라면
- union-find 진행

'''

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def change_water(edges):
    queue = edges
    new_queue = deque()

    while queue:
        row, col = queue.popleft()
        lake[row][col] = '.'
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not waters[nrow][ncol]:
                if lake[nrow][ncol] == 'X':
                    new_queue.append((nrow, ncol))
                else:
                    queue.append((nrow, ncol))
                waters[nrow][ncol] = 1

    return new_queue


def swan_move(swans):
    queue = swans
    new_queue = deque()

    while queue:
        row, col, v_idx = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m:
                if not visited[nrow][ncol]:
                    if lake[nrow][ncol] == 'X':
                        new_queue.append((nrow, ncol, v_idx))
                    else:
                        queue.append((nrow, ncol, v_idx))
                    visited[nrow][ncol] = v_idx
                elif lake[nrow][ncol] != 'X' and visited[nrow][ncol] != v_idx:
                    print(move)
                    exit()

    return new_queue

n, m = map(int, input().split())
lake = [list(input().rstrip()) for _ in range(n)]
swans = deque()
edges = deque()
idx = 0
visited = [[0] * m for _ in range(n)]
waters = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if lake[i][j] == 'X':
            for id in range(len(dr)):
                ni, nj = i + dr[id], j + dc[id]
                if 0 <= ni < n and 0 <= nj < m and lake[ni][nj] != 'X':
                    edges.append((i, j))
                    break
        elif lake[i][j] == 'L':
            swans.append((i, j, idx + 1))
            idx += 1
            visited[i][j] = idx
            waters[i][j] = 1
        else:
            waters[i][j] = 1

move = 0

while True:
    move += 1
    # 1. 엣지 부분 물로 변환
    new_edges = change_water(edges)
    # 2. 백조 이동
    new_swans = swan_move(swans)

    edges = new_edges
    swans = new_swans