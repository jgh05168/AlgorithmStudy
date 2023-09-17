'''
DP

1. dp 배열은 3차원으로 생성하여 각각에 대해서 계산

2. 최종적으로 N, N에 도달했을 때 모두 더해주어 결과 얻기

주의사항 : 계산 전 벽이 있는지 없는지 먼저 판단해야 한다.
    -> 갈 수 있는지 없는지부터 판단한 다음 갈 수 있으면 값 업데이트. 갈 수 없으면 0으로 초기화

    갈 때마다 각각에 대한 값을 모두 더해본다.
        -> 더했는데 값이 0이라면 길이 막힌 경우이므로 프로그램 종료
'''

import sys
input = sys.stdin.readline

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
# 굳이 구현을 할 필요는 없다.
# 그냥 가능한 값만 더해보자.
dp[0][0][1] = 1     # 초기상태

# 가려는 위치에 대해서 가능한 경우를 모두 더한다. 
for i in range(N):
    for j in range(1, N):
        if home[i][j]:
            continue
        # 가로
        if j + 1 < N and not home[i][j + 1]:
            dp[0][i][j + 1] = dp[0][i][j] + dp[2][i][j]
        # 세로
        if i + 1 < N and not home[i + 1][j]:
            dp[1][i + 1][j] = dp[1][i][j] + dp[2][i][j]
        # 대각선
        if i + 1 < N and j + 1 < N:
            if not home[i + 1][j + 1] and not home[i + 1][j] and not home[i][j + 1]:
                dp[2][i + 1][j + 1] = dp[0][i][j] + dp[1][i][j] + dp[2][i][j]

print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])