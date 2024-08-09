'''
전체 길이 - LIS
-> 문제에도 명시되있다.
    - 가장 긴 증가하는 부분 수열(3, 5, 6) 을 제외하고 옮겨준다.
O(n^2) => 200 * 200
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [1] * (n + 1)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(n - max(dp))