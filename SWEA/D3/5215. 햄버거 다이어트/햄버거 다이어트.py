'''
베낭 문제

이제 베낭은 껌이지
'''

t = int(input())
for tc in range(1, t + 1):
    n, l = map(int, input().split())
    ingredient_list = []
    for _ in range(n):
        ingredient_list.append(tuple(map(int, input().split())))    # (점수, 칼로리)

    dp = [[0] * (l + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        value, calory = ingredient_list[i - 1]
        for j in range(l + 1):
            if calory <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - calory] + value)
            else:
                dp[i][j] = dp[i - 1][j]
    print(f'#{tc} {dp[-1][-1]}')