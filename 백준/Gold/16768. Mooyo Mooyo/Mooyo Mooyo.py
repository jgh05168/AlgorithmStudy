'''
이어지는 부분이 k 이상이면 0으로 변경
아니라면 그냥 놔두기

그다음 중력으로 내리기

종료 : 게임이 끝날 때까지 반복
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def gravity():
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if grid[i][j]:
                ci = i
                ni = i + 1
                while ni < n and not int(grid[ni][j]):
                    grid[ni][j] = grid[ci][j]
                    grid[ci][j] = '0'
                    ci = ni
                    ni += 1


def bfs(srow, scol):
    global gameover
    queue = deque()
    queue.append((srow, scol))
    tmp_list = [(srow, scol)]
    visited[srow][scol] = 1
    color = grid[srow][scol]

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and grid[nrow][ncol] == color:
                queue.append((nrow, ncol))
                tmp_list.append((nrow, ncol))
                visited[nrow][ncol] = 1
    if len(tmp_list) >= k:
        gameover = False
        for er, ec in tmp_list:
            grid[er][ec] = '0'


n, k = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
m = 10

while True:
    gameover = True
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and int(grid[i][j]):
                bfs(i, j)

    if gameover:
        break

    gravity()


for i in range(n):
    print(''.join(grid[i]))