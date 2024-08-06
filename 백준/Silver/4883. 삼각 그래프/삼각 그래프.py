'''
그냥 최솟값 찾기
'''

import sys
input = sys.stdin.readline

game = 1
while True:
    n = int(input())
    if not n:
        exit()
    arr = [list(map(int, input().split())) + [int(1e9)] for _ in range(n)]
    arr.append([0] * 4)
    dp = [[int(1e9)] * 5 for _ in range(n + 1)]

    for i in range(n):
        for j in range(1, 4):
            if not i and j == 2:
                dp[i][j] = arr[i][j - 1]
            dp[i][j + 1] = min(dp[i][j] + arr[i][j], dp[i][j + 1])
            dp[i + 1][j + 1] = min(dp[i][j] + arr[i + 1][j], dp[i + 1][j + 1])
            dp[i + 1][j] = min(dp[i][j] + arr[i + 1][j - 1], dp[i + 1][j])
            dp[i + 1][j - 1] = min(dp[i][j] + arr[i + 1][j - 2], dp[i + 1][j - 1])

    print(f'{game}. {dp[n - 1][2]}')
    game += 1