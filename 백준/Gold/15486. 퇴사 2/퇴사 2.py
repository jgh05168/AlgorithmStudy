'''
dp를 2차원 배열로 작성. (일 수 x 누적 가치)
'''

import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]


for i in range(n):
    dp[i] = max(dp[i], dp[i - 1])       # 이전까지의 최댓값을 현재 값에 저장
    # 만약 돈을 받을 수 있는 날이 퇴사일보다 늦다면 continue
    if i + table[i][0] > n:
        continue
    # 최댓값을 비교(오늘 얻은 수익 + 이전에 얻어왔던 수익 vs 나중에 받을 수익)
    # 수익을 받는 날(인덱스)에 값을 업데이트 해야 한다.
    dp[i + table[i][0]] = max(dp[i + table[i][0]], table[i][1] + dp[i])

print(max(dp))