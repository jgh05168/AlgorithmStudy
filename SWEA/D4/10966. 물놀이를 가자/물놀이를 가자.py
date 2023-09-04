T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    dp = [list(input()) for _ in range(N)]

    ans = 0

    limit = 2000 # 최소값 비교 대상, 특정 방향에 물에 없는 경우 대비

    # 오른쪽 아래로 돌면서 min(왼쪽에서 오는 길, 위쪽에서 오는 길)
    for r in range(N):
        for c in range(M):
            if dp[r][c] == "W":
                dp[r][c] = 0
            else:
                # 위에서 왔을때 거리
                up = dp[r - 1][c] if r > 0 else limit
                # 왼쪽에서 왔을때 거리 중에 작은거
                left = dp[r][c - 1] if c > 0 else limit
                dp[r][c] = min(up, left) + 1

    # 왼쪽 위로 돌면서 min(오른쪽에서 오는 길, 아래에서 오는 길)
    for r in range(N - 1, -1, -1):
        for c in range(M - 1, -1, -1):
            if dp[r][c] == "W":
                dp[r][c] = 0
            else:
                # 아래
                down = dp[r + 1][c] if r < N - 1 else limit
                # 오른쪽
                right = dp[r][c + 1] if c < M - 1 else limit
                # 왼쪽 위 물과 거리보다 더 가까운지 계산 추가
                dp[r][c] = min(min(down, right) + 1, dp[r][c])
                ans += dp[r][c]

    print(f"#{tc} {ans}")
