'''
dp

첫째날과 둘째날의 값을 조절하여 마지막 값을 구할 수 있다.
점화식은 문제에 나와있으므로, 값을 비교해가면서 조작해보자
'''

import sys
input = sys.stdin.readline

d, k = map(int, input().split())
dp = [0] * (d + 1)
dp[1] = dp[2] = 1   # 초기값 설정
while True:
    for i in range(3, d + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    # 만약 값이 k보다 작으면, 두번째 값 중가시켜주기
    if dp[d] == k:
        print(dp[1])
        print(dp[2])
        exit()
    elif dp[d] < k:
        dp[2] += 1
    else:
        dp[1] += 1
        dp[2] = dp[1]
