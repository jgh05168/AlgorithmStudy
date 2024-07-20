'''
LIS : 가장 긴 증가하는 부분 수열

- dp를 돌며 이전에 얼마나 증가하였는지에 대한 정보를 저장
- 2중 for문을 사용하여 이전에 연결된 값과 현재 연결된 값 + 1에 대한 최대값을 저장한다.
    - 만약 값이 큰 경우라면, <- 이 조건이 충족해야 함
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 자기 자신 역시 수열의 일부이므로 초기값을 모두 1로 설정
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # 현재 보고 있는 값이 더 큰 경우에만 진행하기
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))