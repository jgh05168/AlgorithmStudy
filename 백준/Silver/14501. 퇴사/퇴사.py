N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(N):
    Ti, Pi = map(int, input().split())
    T[i] = Ti
    P[i] = Pi

dp = [0] * (N + 1)

# 뒤에서부터 확인
for i in range(N - 1, -1, -1):
    if T[i] + i <= N:       # 만약 idx + 상담에 걸리는 날짜 < 퇴사일 + 1
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])     # 현재 price + [idx + 상담까지 걸리는 날의] dp값 과 다음 날의 최대값의 최대값을 비교 후 저장
    else:
        dp[i] = dp[i + 1]       # 상담을 하지 못하므로 dp의 이전 저장값을 불러온다
    # print(dp)
print(dp[0])