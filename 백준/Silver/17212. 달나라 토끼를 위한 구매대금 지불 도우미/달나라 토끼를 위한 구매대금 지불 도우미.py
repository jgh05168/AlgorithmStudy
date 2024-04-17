'''
동전의 개수가 최소가 되도록 지불해야 한다.

-> 동전 게임
백준 동전 2 풀이와 같다.
'''

n = int(input())
dp = [int(1e9)] * (n + 1)
coins = [1, 2, 5, 7]

if n == 0:
    print(0)
else:
    for i in range(4):
        # 현재 있는 동전들보다 n이 작은 경우 넘겨주기
        if coins[i] > n:
            continue
        dp[coins[i]] = 1
        # 현재 동전부터 마지막 만들 수 있는 동전까지 1씩 늘려가며 만들어야 한다.
        for j in range(coins[i], n + 1):
            # 현재 동전 제외하고 만들 수 있는 동전 j 에 현재 동전의 개수 1 증가
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

    print(dp[-1])