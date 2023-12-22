import sys
input = sys.stdin.readline

n = int(input())
dp = [int(1e9)] * 100001
coins = [2, 5]

for i in range(2):
  dp[coins[i]] = 1
  for j in range(coins[i], n + 1):
    dp[j] = min(dp[j], dp[j - coins[i]] + 1)    # 이전에 저장된 코인 정보(현재 동전만큼을 뺀 dp의 인덱스) + 1을 해야된다.

if dp[n] == int(1e9):
  print(-1)
else:
  print(dp[n])