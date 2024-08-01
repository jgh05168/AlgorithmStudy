
n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
dp = [0] * (n + 1)

for i in range(n):
    dp[i] = max(dp[i], dp[i - 1])
    day, val = arr[i]
    if i + day <= n:
        dp[i + day] = max(dp[i + day], dp[i] + val)

print(max(dp))