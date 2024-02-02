from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = 0, 0

def bfs(maps, visited, srow, scol):
    cnt = int(maps[srow][scol])
    queue = deque()
    queue.append((srow, scol))
    visited[srow][scol] = 1
    
    while queue:
        row, col = queue.popleft()
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and maps[nrow][ncol] != 'X':
                cnt += int(maps[nrow][ncol])
                visited[nrow][ncol] = 1
                queue.append((nrow, ncol))
                
    return cnt


def solution(maps):
    global n, m
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    islands = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                islands.append(bfs(maps, visited, i, j))            
    
    if islands == []:
        return [-1]
    else:
        islands.sort()
        return islands
    