T = int(input())


for _ in range(T):
    N = int(input())
    dp = [0] * (N + 1)
    dp_2 = [0] * (N + 1)

    if N <= 3:
        print(1)
    elif 3 < N <= 5:
        print(2)
    else:
        dp[1], dp[2], dp[3] = 1, 1, 1
        dp[4], dp[5] = 2, 2
        for d in range(6, N + 1):
            dp[d] = dp[d - 1] + dp[d - 5]
        print(dp[-1])