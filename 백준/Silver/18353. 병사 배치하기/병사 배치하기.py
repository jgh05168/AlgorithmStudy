'''
LIS : 가장 긴 감소하는 부분수열

1차원 dp : 크면 이전 + 1과 현재로 비교하기
- i < n
- j < i
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))