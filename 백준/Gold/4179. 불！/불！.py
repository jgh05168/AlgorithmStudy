'''
1. 불에 타기 전에 탈출할 수 있는지의 여부
2. 얼마나 빨리 탈출할 수 있는지 결정

- 상하좌우 이동
- 불은 각 지점에서 네 방향으로 확산
- 지훈이의 위치가 index를 벗어난다면 탈출 가능
- 벽이 있는 공간은 통과 불가능
- 시뮬레이션 문제로, 지훈이 움직이자.

사용 알고리즘 : bfs, 이차원 탐색

'''


from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol, fires):
    queue = deque()
    queue.append((srow, scol))

    while True:
        new_queue = deque()
        while queue:
            row, col = queue.popleft()
            # 지훈이 먼저

            # 만약 불이 옮겨붙었다면, 이 위치는 갈 수 없다.
            if visited[row][col] == -1:
                continue

            for d in range(len(dr)):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 > nrow or nrow >= R or 0 > ncol or ncol >= C:
                    return visited[row][col] + 1
                elif 0 <= nrow < R and 0 <= ncol < C and visited[nrow][ncol] == 0 and maze[nrow][ncol] == '.':
                    visited[nrow][ncol] = visited[row][col] + 1
                    new_queue.append((nrow, ncol))

        # 불 이동
        new_fires = deque()
        for frow, fcol in fires:
            for d in range(len(dr)):
                nfrow, nfcol = frow + dr[d], fcol + dc[d]
                if 0 <= nfrow < R and 0 <= nfcol < C and visited[nfrow][nfcol] != -1 and maze[nfrow][nfcol] != '#':
                    visited[nfrow][nfcol] = -1
                    new_fires.append((nfrow, nfcol))

        fires = new_fires
        queue = new_queue

        if not new_queue:
            return 0

# inputs
R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

# 지훈이 찾기
findJ = False
fires = deque()
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            srow, scol = i, j
        elif maze[i][j] == 'F':
            visited[i][j] = -1
            fires.append((i, j))


can_escape = bfs(srow, scol, fires)

if not can_escape:
    print('IMPOSSIBLE')
else:
    print(can_escape)