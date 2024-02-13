'''
내려가면서 가져갈 수 있는 사탕의 최솟값

다 더해가면서 max를 구하면 될듯 ?

'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 1]
dc = [1, 1, 0]

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dp[0][0] = maze[0][0]
queue = deque([(0, 0)])

for i in range(n):
    for j in range(m):
        for d in range(len(dr)):
            ni, nj = i + dr[d], j + dc[d]
            if 0 <= ni < n and 0 <= nj < m:
                dp[ni][nj] = max(dp[ni][nj], dp[i][j] + maze[ni][nj])

print(dp[-1][-1])