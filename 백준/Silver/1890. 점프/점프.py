'''

dfs + dp

도착하면 돌아가면서 길 체크해주기

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dr = [0, 1]
dc = [1, 0]


def dfs(row, col):
    if (row, col) == (n - 1, n - 1):
        return 1
    if dp[row][col]:
        return dp[row][col]

    for d in range(2):
        nrow, ncol = row + dr[d] * board[row][col], col + dc[d] * board[row][col]
        if 0 <= nrow < n and 0 <= ncol < n:
            if not board[nrow][ncol] and (nrow, ncol) != (n - 1, n - 1):
                continue
            dp[row][col] += dfs(nrow, ncol)
    return dp[row][col]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

print(dfs(0, 0))