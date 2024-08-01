'''
n은 0 ~ n까지 있다
dp 점화식 : dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

일단 무조건 점화식 적어보자. (가능한 경우의 수)

'''

n, k = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    for j in range(n + 1):
        if i == 1:
            # 숫자 하나로 만들 수 있는 값은 하나밖에 없다.(자기 자신)
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(dp[-1][-1] % 1000000000)