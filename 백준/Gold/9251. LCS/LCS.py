'''
LCS

풀이 :
1. 2중 for문 사용
2. 만약 글자가 같다면 이전의 순열 + 1
3. 글자가 다르다면 이전에 비교한 값들의 최댓값으로 업데이트
    - ex) dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
'''

import sys
input = sys.stdin.readline

str1 = list(input().rstrip())   # 행
str2 = list(input().rstrip())   # 열
dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:        # 1빼줘야대
            dp[i][j] = dp[i - 1][j - 1] + 1     # 이전까지 비교한 문자열의 위치에 대한 값이 필요하므로 행, 열 모두 -1 해줘야 한다.
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])