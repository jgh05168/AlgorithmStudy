'''
집 칠하는 규칙

1. 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
2. N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
3. i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [[int(1e9)] * 3 for _ in range(n)]

dp[0][0], dp[0][1], dp[0][2] = table[0][0], table[0][1], table[0][2]

for i in range(1, n):
    for j in range(3):
        dp[i][(j + 1) % 3] = min(dp[i][(j + 1) % 3], dp[i - 1][j] + table[i][(j + 1) % 3])
        dp[i][(j + 2) % 3] = min(dp[i][(j + 2) % 3], dp[i - 1][j] + table[i][(j + 2) % 3])

print(min(dp[-1][0], dp[-1][1], dp[-1][2]))