'''
DP로 풀자

ex)

dp[1] = dp[1]
dp[2] = dp[1] + dp[1] | dp[0] + dp[2]
dp[3] = dp[1] + dp[1] + dp[1] | dp[2] + dp[1] | dp[3]
...

'''

N = int(input())
cards = list(map(int, input().split()))
dp = [0] * (N + 1)        # 구매한 카드 개수 별 최대값 저장

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + cards[j - 1])    # cards : 마지막에 몇 장 짜리 카드팩을 사는지

print(dp[-1])