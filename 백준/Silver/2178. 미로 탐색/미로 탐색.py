dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    visited = [[0] * M for _ in range(N)]
    queue = []
    queue.append((srow, scol))
    visited[srow][scol] = 1

    while queue:
        row, col = queue.pop(0)
        for d in range(len(dr)):
            nrow = row + dr[d]
            ncol = col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and maze[nrow][ncol] != 0 and visited[nrow][ncol] == 0:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = visited[row][col] + 1
                if nrow == N - 1 and ncol == M - 1:
                    return visited[nrow][ncol]

    return 0

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

min_loc = bfs(0, 0)

print(min_loc)