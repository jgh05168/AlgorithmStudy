from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solution(maps):
    queue = deque()
    queue.append((0, 0))
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while queue:
        row, col = queue.popleft()
        
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and maps[nrow][ncol]:
                if (nrow, ncol) == (n - 1, m - 1):
                    return (visited[row][col] + 1)
                visited[nrow][ncol] = visited[row][col] + 1
                queue.append((nrow, ncol))
    return -1
    