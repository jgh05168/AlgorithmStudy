N, K = map(int, input().split())
temp = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    if i < K:       # K만큼 더하지 못할 경우
        dp[i] = dp[i - 1] + temp[i]     
    else:           # K개씩 더할 수 있는 경우
        dp[i] = dp[i - 1] - temp[i - K] + temp[i]   # 이전 경우에서 temp[i - K]번째를 뺀 뒤 현재 temp를 더해준다.

# K만큼 더하지 못하는 누적값들은 필요가 없으므로 pop
for i in range(0, K):
    dp.pop(0)   
print(max(dp))