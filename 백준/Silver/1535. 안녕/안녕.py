'''
베낭문제

베낭 : 세준 체력
100 x 20

-- 베낭 문제 복기하기 --
'''

import sys
input = sys.stdin.readline

n = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

dp = [[0] * 100 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(100):
        if L[i] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])