'''
dp에는 동전을 만들 수 있는 경우의 수를 저장
- 만약 현재 동전이 내가 갖고있는 동전보다 크다면
    - 경우 업데이트
'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    dest_coin = int(input())
    dp = [0] * (dest_coin + 1)

    dp[0] = 1
    for coin in coins:
        for i in range(dest_coin + 1):
            if i >= coin:   # 만약 현재 동전보다 크다면,
                dp[i] += dp[i - coin]

    print(dp[-1])