'''
LCS2

문자열의 길이와 문자열이 무엇인지를 찾아야 한다.

풀이 :
맨 마지막부터 탐색한다.
- 만약 위 오른쪽 같은 값이 없다 : ans에 현재 문자열 추가
- 만약 같은 값이 있다 : 위 or 옆으로 이동하여 계속 탐색
'''

import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
n, m = len(str1), len(str2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

# LCS 구하는 DP
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])

ans = []
r, c = n, m
while 0 <= r <= n and 0 <= c <= m:
    # 만약 부분 순열이 같아 업데이트 된 경우라면, 대각선으로 올라가기
    if dp[r][c] != dp[r - 1][c] and dp[r][c] != dp[r][c - 1]:
        ans.append(str1[r - 1])
        r, c = r - 1, c - 1
    # 부분 순열이 같지 않은 경우라면, 더 컸던 값으로 올라가기
    else:
        if dp[r - 1][c] > dp[r][c - 1]:
            r, c = r - 1, c
        else:
            r, c = r, c - 1

for i in range(len(ans) - 1, -1, -1):
    print(ans[i], end="")