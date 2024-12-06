'''
교차하는 애들을 없애주면 된다.
교차하지 않는 최대 길이를 구한 뒤, 전체 길이에서 빼주기
'''

n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])

dp = [1] * n
for i in range(n):
    for j in range(i + 1, n):
        if arr[i][1] < arr[j][1]:
            dp[j] = max(dp[j], dp[i] + 1)

print(n - max(dp))
