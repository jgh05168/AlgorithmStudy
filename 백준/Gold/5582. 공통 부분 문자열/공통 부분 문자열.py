'''
LCS : 최장 공통 부분 수열

문자열은 수열과 다르게, 연속적이기 때문에
문자가 다를 경우 값을 업데이트 해 주는 것이 아닌,
0으로 둔다. 

이후 끝날 때 최댓값이 들었는지 확인하는 과정을 거친다.
'''

str1 = input()
str2 = input()

n, m = len(str1), len(str2)
dp = [[0] * (m + 1) for _ in range(n + 1)]

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if not i or not j:
            dp[i][j] = 0
            continue
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        ans = max(ans, dp[i][j])

print(ans)