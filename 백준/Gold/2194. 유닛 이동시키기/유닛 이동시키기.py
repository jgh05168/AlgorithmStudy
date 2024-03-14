'''
유닛은 상하좌우로 이동 가능

장애물이 설치된 부분이면 허영되지 않는다.

- 최소 이동 횟수를 구하자
맵 : n x m
유닛 : a x b
장애물 k개 주어짐

풀이 :
- 유닛에 대해 bfs진행
진행 방향에 대한 값에 대해 이동 조사.
    - 방향 별로 값을 갖고있자. 그것들에 대해서만 조사해주면 댐
시간복잡도 : 500 * 500 * 10
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    global min_cnt
    queue = deque([(srow, scol)])
    visited[srow][scol] = 0

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            flag = 1    # 다음 위치로 이동할 수 있는지에 대해 조사
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and visited[nrow][ncol] == -1:
                for ui in range(nrow, nrow + a):
                    for uj in range(ncol, ncol + b):
                        if not (0 <= ui < n and 0 <= uj < m) or grid[ui][uj]:
                            flag = 0
                            break
                    if not flag:
                        break
                else:       # 유닛이 이동할 수 있다면,
                    if nrow == erow - 1 and ncol == ecol - 1:   # 도착지라면 종료
                        min_cnt = min(min_cnt, visited[row][col] + 1)
                        return visited[row][col] + 1
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = visited[row][col] + 1


n, m, a, b, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]
for _ in range(k):
    obi, obj = map(int, input().split())
    grid[obi - 1][obj - 1] = 1
srow, scol = map(int, input().split())
erow, ecol = map(int, input().split())

visited = [[-1] * m for _ in range(n)]


min_cnt = int(1e9)
bfs(srow - 1, scol - 1)
if min_cnt == int(1e9):
    print(-1)
else:
    print(min_cnt)