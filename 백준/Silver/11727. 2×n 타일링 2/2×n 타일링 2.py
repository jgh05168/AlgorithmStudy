

N = int(input())
dp = [0] * (N + 1)

if N == 1:
    dp[1] = 1
elif N == 2:
    dp[2] = 3
else:
    dp[1] = 1
    dp[2] = 3
    even_sq = 1
    odd_sq = 1
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + (2 * dp[i - 2])

print(dp[-1] % 10007)