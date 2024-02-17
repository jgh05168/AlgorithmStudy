'''
n, n + 1 위치에 대해서 2차원 dp 진행
'''

import sys
input = sys.stdin.readline


def solution(triangle):
    n = len(triangle)
    dp = [[] * i for i in range(n)]
    for i in range(n):
        for _ in range(len(triangle[i])):
            dp[i].append(0)
    dp[0][0] = triangle[0][0]
    for level in range(1, n):
        for idx in range(len(triangle[level])):
            if not idx:
                dp[level][idx] = dp[level - 1][idx] + triangle[level][idx]
            elif idx == len(triangle[level]) - 1:
                dp[level][idx] = dp[level - 1][idx - 1] + triangle[level][idx]
            else:
                dp[level][idx] = max(dp[level][idx], dp[level - 1][idx - 1] + triangle[level][idx], dp[level - 1][idx] + triangle[level][idx])

    return max(dp[-1])