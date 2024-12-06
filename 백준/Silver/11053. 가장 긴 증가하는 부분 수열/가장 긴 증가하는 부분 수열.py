n = int(input())
arr = list(map(int, input().split()))

# 생각해야 할 부분 : 증가하는 경우에 1씩 더해준다

dp = [0] * n

for i in range(n):
    dp[i] = max(dp[i], 1)
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))