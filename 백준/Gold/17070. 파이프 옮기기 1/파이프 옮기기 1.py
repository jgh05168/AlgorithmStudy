import sys
from collections import deque
input = sys.stdin.readline

# 가로일 경우
wdr = [0, 1]
wdc = [1, 1]

# 세로일 경우
hdr = [1, 1]
hdc = [0, 1]

# 대각선일 경우
diagdr = [0, 1, 1]
diagdc = [1, 0, 1]


def dfs(row, col, dir):
    global cnt
    if (row, col) == (N - 1, N - 1):
        cnt += 1
    else:
        # 가로로 온 경우
        if dir == 0:
            for d in range(len(wdr)):
                nrow, ncol = row + wdr[d], col + wdc[d]
                if d == 0:      # 가로
                    if 0 <= nrow < N and 0 <= ncol < N and grid[nrow][ncol] == 0:
                        dfs(nrow, ncol, 0)
                elif d == 1:    # 대각선
                    if 0 <= nrow < N and 0 <= ncol < N and (grid[nrow][ncol] == 0 and grid[nrow - 1][ncol] == 0 and grid[nrow][ncol - 1] == 0):
                        dfs(nrow, ncol, 2)

        # 세로로 온 경우
        elif dir == 1:
            for d in range(len(hdr)):
                nrow, ncol = row + hdr[d], col + hdc[d]
                if d == 0:      # 세로
                    if 0 <= nrow < N and 0 <= ncol < N and grid[nrow][ncol] == 0:
                        dfs(nrow, ncol, 1)
                elif d == 1:    # 대각선
                    if 0 <= nrow < N and 0 <= ncol < N and (grid[nrow][ncol] == 0 and grid[nrow - 1][ncol] == 0 and grid[nrow][ncol - 1] == 0):
                        dfs(nrow, ncol, 2)

        # 대각선으로 온 경우
        elif dir == 2:
            for d in range(len(diagdr)):
                nrow, ncol = row + diagdr[d], col + diagdc[d]
                if d == 0 or d == 1:  # 세로
                    if 0 <= nrow < N and 0 <= ncol < N and grid[nrow][ncol] == 0:
                        dfs(nrow, ncol, d)
                elif d == 2:  # 대각선
                    if 0 <= nrow < N and 0 <= ncol < N and (
                            grid[nrow][ncol] == 0 and grid[nrow - 1][ncol] == 0 and grid[nrow][ncol - 1] == 0):
                        dfs(nrow, ncol, d)


N = int(input().strip())

'''
0 : 가로
1 : 세로
2 : 대각선
'''
grid = [list(map(int, input().split())) for _ in range(N)]
if grid[N - 1][N - 1] == 1:
    print(0)
else:
    cnt = 0
    dfs(0, 1, 0)
    print(cnt)