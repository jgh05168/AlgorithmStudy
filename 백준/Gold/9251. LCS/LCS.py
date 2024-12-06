'''
LCS

모두의 부분 수열이 되는 수열 중 가장 긴 것 찾기
고려해야 할 사항 : 한 개씩 비교해가며 맞나 아닌가를 판단해야함

만약 현재 문자가 다른 문자와 같다면 ? dp[i - 1][j - 1] + 1 진행 => 현재 오고있던 값에 영향을 미치면 안된다.
다르다면, dp[i - 1][j]와 dp[i][j - 1] 비교
'''

s1, s2 = input(), input()
n, m = len(s1), len(s2)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])