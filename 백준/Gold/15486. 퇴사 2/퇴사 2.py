'''

'''

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    dp[i] = max(dp[i], dp[i - 1])
    t, p = arr[i]
    if i + t > n: continue
    else:
        dp[i + t] = max(dp[i] + p, dp[i + t])
print(max(dp))