'''
테트로미노

dfs로 한번, 인접노드로 한번 하여 한 노드에서의 최대값을 구한다.

dfs

1. 시간초과가 남
    -> 배열 중 가장 큰 값을 구한 뒤 매 계산마다 max_val과 현재 값 + (배열의 가장 큰 값 * 4 - 시도)를 진행한다.
'''

import sys
input = sys.stdin.readline


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# ㅗ 모양을 뺀 나머지 모양들 값 구하기
def dfs(polynomio, val, row, col):
    global max_val
    if polynomio == 4:
        max_val = max(max_val, val)
        return

    if max_val and max_val > val + (max_grid * (4 - polynomio)):
        return

    for d in range(len(dr)):
        nrow, ncol = row + dr[d], col + dc[d]
        if 0 <= nrow < N and 0 <= ncol < M and not visited[nrow][ncol]:
            visited[nrow][ncol] = 1
            dfs(polynomio + 1, val + grid[nrow][ncol], nrow, ncol)
            visited[nrow][ncol] = 0

# ㅗ 모양 값 구하기
def adj(row, col):
    global max_val

    idx = 0
    for _ in range(4):
        val = grid[row][col]
        for d in range(3):      # 3번만 반복해야 한다.
            nrow, ncol = row + dr[(idx + d) % 4], col + dc[(idx + d) % 4]
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M:
                break
            val += grid[nrow][ncol]

        max_val = max(max_val, val)
        idx += 1


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_grid = max(map(max, grid))
max_val = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, grid[i][j], i, j)
        adj(i, j)
        visited[i][j] = 0
print(max_val)