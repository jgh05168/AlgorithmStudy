'''
1. 여러 단원을 융합한 문제는 출제 x
2. 한 단우너에 한 문제, 모든 내용을 알아야 풀 수 있음

예상 공부 시간보다 더 많이 공부하면 맞출 수 있다.

최대 점수 구하기

풀이:
100 x 10000
공부시간, 배점

냅색 알고리즘
배점만큰 돌려가며 예상 공부시간을 넣을 수 있으면, 업데이트 해본다.
'''

import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = [0]
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
dp = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    study_time, point = arr[i]
    for j in range(i, t + 1):
        # 못넣는 경우,
        if study_time > j:
            dp[i][j] = dp[i - 1][j]
        # 넣을 수 있는 경우
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - study_time] + point)

print(dp[-1][-1])