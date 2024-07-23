'''
냅색 알고리즘
남은기간 N일, 전부 읽는데 소요되는 일 수 / 페이지 수
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
book = [(0, 0)]
for _ in range(m):
    book.append(tuple(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        # 넣을 수 있어야 된다.
        if book[i][0] <= j:
            # 넣을 수 있는 경우, 이전 무게 까지의 값(현재 무게 - 입력 무게) + 현재 무게의 값 더해줘야 함
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - book[i][0]] + book[i][1])
        else:
            dp[i][j] = dp[i - 1][j]
            
print(dp[-1][-1])