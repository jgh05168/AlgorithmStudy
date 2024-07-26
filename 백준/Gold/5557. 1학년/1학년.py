'''
1학년

dp 행은 수식에 대한 값, 열은 0 ~ 20 사이 로 설정한다.
출력은 마지막 값을 출력한다.

경우의 수를 구하는 문제의 경우, dp 테이블에 가능한 모든 경우의 수 테이블을 만들어서,
그 안에서 모든 값을 해결할 수 있어야 한다.

[추가]
업데이트 진행할 때, 중복된 경우라도 for문 돌면서 한 번 더 계산해 주어야 한다.
    -> 이전 값을 더해주는 방식으로 누적한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
eq = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n - 1)]
# 맨 처음 값 세팅
dp[0][eq[0]] = 1
# i와 j의 범위 설정에 주의하기
for i in range(1, n - 1):
    for j in range(21):
        # 이전에 수식 계산이 된 값이라면,
        if dp[i - 1][j]:
            # 덧셈, 뺄셈 둘 다 해보기
            # 뺄셈
            if j - eq[i] >= 0:
                dp[i][j - eq[i]] += dp[i - 1][j]
            # 덧셈
            if j + eq[i] <= 20:
                dp[i][j + eq[i]] += dp[i - 1][j]

print(dp[-1][eq[-1]])