'''
로봇 탐사하기

조건 : 한번 지나간 좌표는 다시 돌아갈 수 없다
    ==> 한 층에서는 일방통행만 가능하다는 뜻

    왼 -> 오
    오 -> 왼
    각 행 별 누적값 탐사해본 뒤, 두 방향의 최댓값 정보를 dp에 저장 (경로는 일방통행이므로 중복 방문하지 않는다)
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

# 0. 첫번째 행 누적합 진행(init)
dp[0][0] = grid[0][0]
for i in range(1, m):
    dp[0][i] = dp[0][i - 1] + grid[0][i]

# 1. 각 행 돌면서 방향 별 누적합 구하기
for i in range(1, n):
    right, left = [0] * m, [0] * m

    right[0], left[-1] = dp[i - 1][0] + grid[i][0], dp[i - 1][-1] + grid[i][-1]
    # 1-1. 오른쪽 방향으로 이동
    for j in range(1, m):
        right[j] = max(dp[i - 1][j], right[j - 1]) + grid[i][j]
    # 1-2. 왼쪽 방향으로 이동
    for j in range(m - 2, -1, -1):
        left[j] = max(dp[i - 1][j], left[j + 1]) + grid[i][j]

    # 1-3. dp에 이동 간 max값 업데이트하기
    for j in range(m):
        dp[i][j] = max(right[j], left[j])

print(dp[-1][-1])