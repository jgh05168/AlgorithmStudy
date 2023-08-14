n = int(input())
dp = [0] * (n + 1)

if n == 1:
    dp[1] = 1
elif n == 2:
    dp[2] = 2
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]       # 점화식을 구하기

print(dp[-1] % 10007)
