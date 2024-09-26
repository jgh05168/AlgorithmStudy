'''
dp
'''

import heapq

def solution(x, y, n):
    dp = [1000001] * 3000003
    
    dp[x] = 0
    for i in range(x, y + 1):
        dp[i + n] = min(dp[i + n], dp[i] + 1)
        dp[i * 3] = min(dp[i * 3], dp[i] + 1)
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)
    
    if dp[y] == 1000001:
        return -1
    else:
        return dp[y]
