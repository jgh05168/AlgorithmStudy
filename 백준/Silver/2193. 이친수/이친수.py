'''
규칙이 존재한다.

1 : 1
2 : 1
3 : 2
4 : 3
5 : 8
6 : 13

... -> 피보나치 수열로 풀면 된다.
'''

n = int(input())
dp = [0] * n
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    dp[0], dp[1] = 1, 1
    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1]

    print(dp[-1])