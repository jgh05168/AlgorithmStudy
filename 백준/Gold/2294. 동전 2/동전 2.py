'''
동전 리스트를 반복
현재 동전부터 한 칸 씩 더해가면서 max값 비교

'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [int(1e9)] * (k + 1)   # 인덱스 : 동전의 가치
arr = [int(input()) for _ in range(n)]

for i in range(n):
  if arr[i] <= k:
    dp[arr[i]] = 1
  for j in range(arr[i], k + 1):
    dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[k] == int(1e9):
  print(-1)
else:
  print(dp[k])