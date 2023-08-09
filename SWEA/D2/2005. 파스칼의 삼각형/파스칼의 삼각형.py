T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    dp = [[1] * i for i in range(1, N + 1)]

    # 3번째 줄부터 시작(1, 2번째 줄은 모두 1을 갖는다)
    for i in range(2, N):
        for j in range(1, len(dp[i]) - 1):      # 양 끝 값을 제외한 나머지 값들에 대해서
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]      # 이전 줄의 왼쪽과 오른쪽 값을 더해준다

    print(f'#{tc}')
    for i in range(len(dp)):
        print(*dp[i])