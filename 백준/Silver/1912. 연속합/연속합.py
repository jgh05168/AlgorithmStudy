n = int(input())
per = list(map(int, input().split()))

dp = [0] * n
dp[0] = per[0]      # 초기 값 저장
for i in range(1, n):
    # 이전까지 더했던 연속값의 합 + 현재값 & 현재값 의 최대값을 dp에 저장
    dp[i] = max(per[i], per[i] + dp[i - 1])     
    
print(max(dp))