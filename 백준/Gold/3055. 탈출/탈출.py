'''
물 먼저 채우고 고슴도치 이동

bfs

'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(status, animal, something):
    new_queue = deque()
    queue = status
    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < r and 0 <= ncol < c and visited[nrow][ncol] == -1 and grid[nrow][ncol] != 'X':
                # 물인 경우
                if not something:
                    # 갈 수 있는 모든 부분 이동
                    if grid[nrow][ncol] == 'D':
                        continue
                    else:
                        new_queue.append((nrow, ncol))
                        visited[nrow][ncol] = visited[row][col] + 1
                        grid[nrow][ncol] = '*'
                # 고슴도치인 경우
                else:
                    if grid[nrow][ncol] == 'D':
                        print(visited[row][col] + 1)
                        exit()
                    elif grid[nrow][ncol] == '*':
                        continue
                    else:
                        new_queue.append((nrow, ncol))
                        visited[nrow][ncol] = visited[row][col] + 1

    if not something:
        return new_queue, deque(set(list(animal)).difference(set(list(new_queue))))
    else:
        return new_queue



r, c = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(r)]
visited = [[-1] * c for _ in range(r)]

animal = deque()
home = (0, 0)
waters = deque()
for i in range(r):
    for j in range(c):
        if grid[i][j] == '*':
            waters.append((i, j))
            visited[i][j] = 0
        elif grid[i][j] == 'S':
            animal.append((i, j))
            visited[i][j] = 0
        elif grid[i][j] == 'D':
            home = (i, j)

# 한번씩만 돌아야 함
while animal:
    waters, animal =  bfs(waters, animal, 0)     # 물부터 돌아보기
    animal = bfs(animal, animal, 1)

print('KAKTUS')