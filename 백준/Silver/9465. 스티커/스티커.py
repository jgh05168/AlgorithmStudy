'''
스티커를 떼면 4방향 스티커는 사용할 수 없게 된다.

바로 옆 칸, 바로 옆옆칸의 크기를 비교해보아 더 큰 값을 더해준다.
'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    if n > 1:
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] += dp[0][0] + stickers[1][1]
        for i in range(2, n):
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + stickers[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i]

    print(max(dp[0][-1], dp[1][-1]))