N = int(input())
glasses = [0]
for _ in range(N):
    glasses.append(int(input()))

dp = [0] * (N + 1)  # dp 생성

# N == 1
if N == 1:
    print(glasses[1])
# N == 2
elif N == 2:
    print(glasses[1] + glasses[2])

# N 이 3 이상일 경우
else:
    # 이 경우들은 dp 없이 존재할 수 있다.
    dp[1] = glasses[1]
    dp[2] = glasses[2] + dp[1]

    # case를 2가지로 나누어서 그 중 큰 값을 dp에 저장
    for i in range(3, N + 1):
        # 잔에 술이 없다면,
        if glasses[i] == 0:
            dp[i] = dp[i - 1]   # 이전 경우가 내가 현재 마실 수 있는 최대 양
        else:
            case1 = dp[i - 2] + glasses[i]      # 한 칸 건너뛰고 포도주를 마신 경우
            case2 = glasses[i] + glasses[i - 1] + dp[i - 3]     # 현재 집은 glass 이전에 포도주를 마신 경우 --> dp의 3번째 이전 값을 들고와야한다.
                                                                # 먹 안먹 먹 먹(현재) : 첫번째 먹이 dp값
            case3 = dp[i - 1]                                   # 현재 잔을 안마시고 쉬어가는 경우

            dp[i] = max(case1, case2, case3)

    print(dp[N])