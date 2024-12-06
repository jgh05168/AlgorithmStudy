'''
n x n 크기 대나무숲
상하좌우 이동
그 전 지역보다 대나무가 많이 있어야 한다.
판다가 최대한 많은 칸을 방문하기 위한 칸의 최댓값 개수 구하기

500 x 500, dp로 풀기
dfs + dp 방식으로 풀기
이동할 수 있는 경우의 수에 대해서 저장하는 것이다. !!!!!!!

'''

import sys
sys.setrecursionlimit(10**8)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    # 1. dp에 값이 저장되어있다면 return
    if dp[r][c]:
        return dp[r][c]

    for d in range(len(dr)):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and grid[r][c] < grid[nr][nc]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)

    return dp[r][c]


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dfs(i, j)


print(max(map(max, dp)) + 1)