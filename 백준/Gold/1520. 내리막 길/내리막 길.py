'''
내리막길의 모든 경로를 찾는다.

dfs 사용.
도착지까지 방문한 경우 1 리턴. 아닌 경우 그 위치에서 갈 수 있는 수 리턴

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(row, col):
    if (row, col) == (n - 1, m - 1):
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if can_go[row][col] != -1:
        return can_go[row][col]

    path = 0
    # 네 방향에서 갈 수 있는 길의 개수를 저장
    for i in range(4):
        nrow, ncol = row + dr[i], col + dc[i]
        if 0 <= nrow < n and 0 <= ncol < m and grid[row][col] > grid[nrow][ncol]:
            path += dfs(nrow, ncol)

    can_go[row][col] = path
    return can_go[row][col]


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
can_go = [[-1] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dfs(0, 0)
print(can_go[0][0])

