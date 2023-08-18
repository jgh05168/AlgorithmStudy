dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    visited = [[False] * N for _ in range(N)]
    queue = []
    visited[srow][scol] = True
    queue.append((srow, scol))

    while queue:
        row, col = queue.pop(0)
        for d in range(len(dr)):
            nrow = row + dr[d]
            ncol = col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol] and maze[nrow][ncol] != 1:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = True
                if maze[nrow][ncol] == 3:
                    return 1

    return 0

for _ in range(10):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(16)]

    for i in range(1, N):
        for j in range(1, N - 1):
            if maze[i][j] == 2:
                s_row, s_col = i, j
                break

    print(f'#{tc} {bfs(s_row, s_col)}')