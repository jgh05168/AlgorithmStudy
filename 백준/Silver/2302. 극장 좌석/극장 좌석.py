'''
빈 칸 개수 세어주기 + 칸 개수만큼 점화식으로 곱해주기
1, 2, 3, 5, 8, 12, ...
'''

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
seats = [0] * (n + 1)
vips = set()
for _ in range(m):
    seats[int(input())] = 1

dp = [0] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i - 2] + dp[i - 1]

empty = 0
ans = 1
for i in range(1, n + 1):
    if not seats[i]:
        empty += 1
    else:
        ans *= dp[empty]
        empty = 0
print(ans * dp[empty])