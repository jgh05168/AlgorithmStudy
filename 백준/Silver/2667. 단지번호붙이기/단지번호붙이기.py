'''
bfs 탐색하며 상하좌우 집 개수 측정
sort() 정렬
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol))
    tmp = 1
    visited[srow][scol] = 1

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol] and maps[nrow][ncol]:
                tmp += 1
                visited[nrow][ncol] = 1
                queue.append((nrow, ncol))
    return tmp


n = int(input())
maps = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnts = []

cnt = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] and not visited[i][j]:
            cnts.append(bfs(i, j))
            cnt += 1

cnts.sort()
print(cnt)
for i in cnts:
    print(i)