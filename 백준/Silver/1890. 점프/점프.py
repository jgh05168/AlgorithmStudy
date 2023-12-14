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
        return 1        # 목적지에 도달했다면 갈 수 있다(1) 리턴
    if dp[row][col]:        # 만약 경로를 이미 탐색한 적이 있다면
        return dp[row][col]     # 값 바로 리턴

    for d in range(2):
        nrow, ncol = row + dr[d] * board[row][col], col + dc[d] * board[row][col]
        if 0 <= nrow < n and 0 <= ncol < n:
            if not board[nrow][ncol] and (nrow, ncol) != (n - 1, n - 1):
                continue
            dp[row][col] += dfs(nrow, ncol)     # 현재 좌표에서 이동했을 때 갈 수 있는 경우를 더해준다.
    return dp[row][col]     # 갈 수 있는 곳 다 가본 뒤 얻어지는 총 경로 개수를 반환해준다.
                            # 이전 좌표로 경로 업데이트를 시켜주는 과정.


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

print(dfs(0, 0))
