'''
각 지점에 대해서 bfs를 돌려보자

dfs + dp
- 출발지부터 몇 칸 갔는지를 세어본다
- 만약 이미 방문했던 지점이라면 반환
- 아닌경우 max를 사용하여 순차적으로 dp 업데이트

정답 : 판다가 랜덤한 위치에서 최대한 많이 이동할 수 있는 칸의 수의 최댓값
'''


from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(row, col):
    if memo[row][col]:         # main의 반복문과 마찬가지로 이미 방문한 지점이라면 현재 길보다 더 많이 갔다는 것이므로 반환해준다.
        return memo[row][col]

    memo[row][col] = 1
    for d in range(len(dr)):
        nrow = row + dr[d]
        ncol = col + dc[d]
        if 0 <= nrow < n and 0 <= ncol < n and forest[row][col] < forest[nrow][ncol]:
            memo[row][col] = max(memo[row][col], dfs(nrow, ncol) + 1)
    return memo[row][col]


n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * n for _ in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        if not memo[i][j]:      # 이미 갔던 기록이 있다면, 그 경로가 현재 경로보다 더 많이 갔다는 것을 의미하므로 갈 필요가 없다.
            result = max(result, dfs(i, j))


print(max(map(max, memo)))
