'''
다음 자리에 몇 가지가 나올 수 있는지에 대해 업데이트 해주기
2차원 배열
'''

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(10):
        if i == 1:
            if not j:
                dp[i][j] = 0
            else:
                dp[i][j] = 1
        else:
            if not j:
                dp[i][j] = dp[i - 1][1]
            elif j == 9:
                dp[i][j] = dp[i - 1][8]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[-1]) % 1000000000)