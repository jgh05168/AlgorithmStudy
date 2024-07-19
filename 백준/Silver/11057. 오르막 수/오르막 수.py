'''
다음 자리에 몇 가지가 나올 수 있는지에 대해 업데이트 해주기
2차원 배열
슬라이딩 윈도우 기법 사용하기
'''

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(10):
        if i == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = sum(dp[i - 1][j:10])

print(sum(dp[-1]) % 10007)