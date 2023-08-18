# def find_start(N):
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 return i, j
#

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def bfs(srow, scol, N):
    visited = [[False] * N for _ in range(N)]
    queue = []
    queue.append((srow, scol))
    visited[srow][scol] = True

    while queue:
        row, col = queue.pop(0)
        for d in range(len(drow)):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < N and 0 <= ncol < N and visited[nrow][ncol] == False and maze[nrow][ncol] != 1:
                if maze[nrow][ncol] == 3:
                    return 1
                queue.append((nrow, ncol))
                visited[nrow][ncol] = True

    return 0


for _ in range(1, 11):
    tc = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]

    srow, scol = 1, 1
    ans = bfs(srow, scol, N)
    print(f'#{tc} {ans}')