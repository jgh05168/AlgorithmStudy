'''
길이를 찾으려는 숫자가 비교할 숫자보다 크면,
그 숫자가 가지고 있는 길이+1과 자신이 길이를 비교해서 큰 값으로 최신화 한다.

[핵심] dp 배열에는 부분수열의 길이 정보를 저장
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))