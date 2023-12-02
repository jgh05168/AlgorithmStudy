'''
배열 회전 알고리즘

1. zip 사용하지 않는 경우

    1. 시계 방향
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[N - j - 1][i]

    2. 반시계 방향
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[j][N - i - 1]

2. zip을 사용하는 경우

    1. 시계 방향
    new_arr = list(map(list, zip(*arr[::-1])))

    2. 반시계 방향
    new_arr = list(map(list, zip(*arr)))[::-1]
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def rotate(row, col):
    tmp_grid = []
    for i in range(row, row + 2 ** L):
        tmp_grid.append(grid[i][col:col + 2 ** L])

    tmp_grid = list(zip(*tmp_grid[::-1]))
    ti = 0
    for ui in range(row, row + 2 ** L):
        tj = 0
        for uj in range(col, col + 2 ** L):
            new_grid[ui][uj] = tmp_grid[ti][tj]
            tj += 1
        ti += 1


def bfs(srow, scol):
    queue = deque()
    visited[srow][scol] = 1
    queue.append((srow, scol))
    ice_amount = grid[srow][scol]
    grid_cnt = 1

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < 2 ** N and 0 <= ncol < 2 ** N and not visited[nrow][ncol] and grid[nrow][ncol] > 0:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = 1
                ice_amount += grid[nrow][ncol]
                grid_cnt += 1

    return ice_amount, grid_cnt


N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2 ** N)]
L_list = list(map(int, input().split()))

# 파이어스톰 시전
for L in L_list:
    # 부분격자로 나눈 뒤 90도 회전을 한번에 진행
    new_grid = [[0] * 2 ** N for _ in range(2 ** N)]
    for row in range(0, 2 ** N, 2 ** L):
        for col in range(0, 2 ** N, 2 ** L):
            rotate(row, col)

    melting = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            adj_ice = 0
            if new_grid[i][j] > 0:
                for d in range(len(dr)):
                    ni, nj = i + dr[d], j + dc[d]
                    if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N:
                        if new_grid[ni][nj] > 0:
                            adj_ice += 1

                if adj_ice < 3:
                    melting.append((i, j))

    for mrow, mcol in melting:
        new_grid[mrow][mcol] -= 1


    grid = new_grid


# 가장 큰 덩어리 찾기
visited = [[0] * 2 ** N for _ in range(2 ** N)]
total_ice = 0
max_grid = 0
for irow in range(2 ** N):
    for icol in range(2 ** N):
        if grid[irow][icol] and not visited[irow][icol]:
            tmp_ice, tmp_grid = bfs(irow, icol)
            total_ice += tmp_ice
            if max_grid < tmp_grid:
                max_grid = tmp_grid

print(total_ice)
print(max_grid)