'''
가치의 합이 k가 되는 경우의 수 구하기
동전을 하나씩 넣는다고 생각하자.

DP문제를 잘 해결하기 위해선 2가지가 중요한 것 같다.

1. 점화식을 세우는 것
2. dp[i]에 도달하기 이전인 0 ~ i - 1 까지는 최적의 값이 저장되었다고 확신하는 것
'''


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
for _ in range(n):
    coin = int(input())
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]   # 이미 만들 수 있는 경우 + 현재 동전 하나 추가해 준 경우.
print(dp[k])



