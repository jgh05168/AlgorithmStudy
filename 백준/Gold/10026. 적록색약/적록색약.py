dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def normal(srow, scol, visited, color):
    queue = []
    queue.append((srow, scol))
    visited[srow][scol] = True

    while queue:
        row, col = queue.pop(0)
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol] and picture[nrow][ncol] == color:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = True

    return 1


def problem(srow, scol, visited, color):
    queue = []
    queue.append((srow, scol))
    visited[srow][scol] = True

    while queue:
        row, col = queue.pop(0)
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if color == 'B':
                if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol] and picture[nrow][ncol] == color:
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = True
            else:
                if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol] and picture[nrow][ncol] != 'B':
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = True

    return 1

N = int(input())

picture = [list(input()) for _ in range(N)]
normal_visited = [[False] * N for _ in range(N)]
problem_visited = [[False] * N for _ in range(N)]

normal_look = 0
problem_look = 0
for i in range(N):
    for j in range(N):
        color = picture[i][j]
        if not normal_visited[i][j]:
            normal_look += normal(i, j, normal_visited, color)
        if not problem_visited[i][j]:
            problem_look += problem(i, j, problem_visited, color)

print(normal_look, problem_look)