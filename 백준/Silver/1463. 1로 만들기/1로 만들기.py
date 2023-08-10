X = int(input())

dp = [0] * (X + 1)

# bottom - up
for i in range(2, len(dp)):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:      # 2로 나누어 떨어질 경우
        dp[i] = min(dp[i], dp[i // 2] + 1)      # 이전 값에서 1을 더한 값, 2로 나눈 값 + 1 의 최소값을 비교
    if i % 3 == 0:      # 3으로 나누어 떨어질 경우
        dp[i] = min(dp[i], dp[i // 3] + 1)      # 이전 값에서 1을 더한 값, 3로 나눈 값 + 1 의 최소값을 비교
    # print(dp)
print(dp[-1])