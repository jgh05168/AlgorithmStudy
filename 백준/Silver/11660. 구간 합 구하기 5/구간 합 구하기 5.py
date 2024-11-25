'''
2차원 누적합

이건공식을 외웠지롱 : arr[x][y] = 원래값 + arr[x - 1][y] + arr[x][y - 1] - arr[x - 1][y - 1]
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = grid[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 구간합 출력하기
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])
