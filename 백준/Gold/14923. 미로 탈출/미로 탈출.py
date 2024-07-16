
'''
벽뚫기

벽을 한 번만 뚫을 수 있음 -> visited를 2개 만들자(3차원)

'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x, 0, 1))
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[y][x][1] = True
    while q:
        y, x, cnt, magic = q.popleft()
        if (y, x) == (ey - 1, ex - 1):
            return cnt
        for i in range(4):
            ny, nx = y + dr[i], x + dc[i]
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx][magic]:
                    continue
                if grid[ny][nx] == 1 and magic == 1:
                    visited[ny][nx][0] = True
                    q.append((ny, nx, cnt + 1, magic - 1))
                elif grid[ny][nx] == 0:
                    visited[ny][nx][magic] = True
                    q.append((ny, nx, cnt + 1, magic))

    return -1

n, m = map(int, input().split())
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

print(bfs(sy - 1, sx - 1))