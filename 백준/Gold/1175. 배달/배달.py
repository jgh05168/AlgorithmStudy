'''
민식이는 같은 방향으로 2번 갈 수 없다.

visited 배열을 4방향을 갖는 3차원 배열로 설정 -> 두 번 이상 가는 경우는 갈 수 없는 경우로 판단.
c를 만나면 visited 초기화
'''

from collections import deque
import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol, sd, time):
    global presents, min_time
    queue = []
    heapq.heappush(queue, (time, srow, scol, sd))
    visited = [[[-1] * m for _ in range(n)] for _ in range(4)]
    if sd == -1:
        for i in range(4):
            visited[i][srow][scol] = 0
    else:
        visited[sd][srow][scol] = 0

    while queue:
        cur_t, row, col, cur_d = heapq.heappop(queue)

        for d in range(len(dr)):
            if d == cur_d:
                continue
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and visited[d][nrow][ncol] == -1 and blocks[nrow][ncol] != '#':
                if blocks[nrow][ncol] == 'C':
                    presents -= 1
                    time += (visited[cur_d][row][col] + 1)
                    if presents:
                        blocks[nrow][ncol] = '.'
                        bfs(nrow, ncol, d, cur_t + 1)
                        blocks[nrow][ncol] = 'C'
                        presents += 1
                    else:
                        min_time = min(min_time, cur_t + 1)
                        presents += 1
                        return
                else:
                    queue.append((cur_t + 1, nrow, ncol, d))
                    visited[d][nrow][ncol] = visited[cur_d][row][col] + 1


n, m = map(int, input().split())
blocks = [list(input().rstrip()) for _ in range(n)]
min_time, presents = int(1e9), 2
sr, sc = -1, -1
for i in range(n):
    for j in range(m):
        if blocks[i][j] == 'S':
            sr, sc = i, j
            break
    if (sr, sc) != (-1, -1):
        break

bfs(sr, sc, -1, 0)

if min_time != int(1e9):
    print(min_time)
else:
    print(-1)