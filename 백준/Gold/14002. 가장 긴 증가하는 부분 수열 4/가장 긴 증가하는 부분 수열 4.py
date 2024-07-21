'''
LIS

경로 저장 배열을 사용해서 풀어보면 어떨까??
    -> 값을 업데이트 할 떄 idx를 저장한다.
    -> max 대신 직접 조건문을 사용해 비교한다.

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
path = [-1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j] + 1:
                path[i] = j
                dp[i] = dp[j] + 1


max_v = 0
max_idx = 0
for i in range(n):
    if max_v < dp[i]:
        max_idx = i
        max_v = dp[i]
print(max_v)
path_ans = []
while True:
    if path[max_idx] == -1:
        path_ans.append(arr[max_idx])
        break
    path_ans.append(arr[max_idx])
    max_idx = path[max_idx]

path_ans.sort()
print(*path_ans)
