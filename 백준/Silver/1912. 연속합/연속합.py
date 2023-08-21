n = int(input())
per = list(map(int, input().split()))

dp = [0] * n
dp[0] = per[0]
for i in range(1, n):
    dp[i] = max(per[i], per[i] + dp[i - 1])

print(max(dp))