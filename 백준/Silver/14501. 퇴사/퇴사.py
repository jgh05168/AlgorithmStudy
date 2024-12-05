n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

### 상담을 받거나, 받지 않거나

dp = [0] * (n + 1)
for i in range(n):
    if i + arr[i][0] > n:
        continue
    else:
        dp[i] = max(dp[i - 1], dp[i])
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1])

print(max(dp))