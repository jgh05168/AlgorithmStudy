'''
dp

단순히 max 함수 써서 진행
'''

import sys
input = sys.stdin.readline


n = int(input())
dp = [[0] * n for _ in range(n)]
for i in range(n):
  inp = list(map(int, input().split()))
  if not i:
    dp[i][i] = inp[i]
  else:
    for j in range(len(inp)):
      if j == 0:
        dp[i][j] = max(dp[i][j], dp[i - 1][0] + inp[j])
      elif j == len(inp):
        dp[i][j] = max(dp[i][j], dp[i - 1][-1] + inp[j])
      else:
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + inp[j], dp[i - 1][j] + inp[j])

print(max(dp[-1]))
