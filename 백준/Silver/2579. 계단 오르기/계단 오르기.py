N = int(input())

dp = [0] * N

stairs = list(int(input()) for _ in range(N))

# 계단이 2개밖에 없는 경우
if len(stairs) == 1:
    print(stairs[0])
elif len(stairs) == 2:
    print(stairs[0] + stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = dp[0] + stairs[1]
    for i in range(2, N):
        # 첫번쨰 인자 : stairs[i]의 이전 계단을 밟고 올라온 경우 -> 현재 계단보다 3계단 낮은 dp값에서 올라온다. (밟 안밟 밟 밟)
        # 두번쨰 인자 : stairs[i]의 전전 계단을 밟고 올라온 경우 -> 현재 계단보다 두계단 낮은 dp값에서 올라온다. (밟 안밟 밟)
        # dp배열 : 순차적으로 올라온 값들 중 최고값들의 배열
        dp[i] = max(stairs[i] + stairs[i - 1] + dp[i - 3], stairs[i] + dp[i - 2])

    # print(stairs)
    print(dp[-1])