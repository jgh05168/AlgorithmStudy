
# 방향벡터 생성(대각선의 경우 그림을 구분하는 데 사용되는 정보)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 일반인의 bfs -- 모든 색에 대해 구분이 가능하다.
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


# 적녹색약의 bfs -- 파랑색과 그 외 나머지 색에 대한 case를 구분지어야 한다.
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
normal_visited = [[False] * N for _ in range(N)]        # 정상인 기준 방문배열
problem_visited = [[False] * N for _ in range(N)]       # 적녹색약인 기준 방문배열

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
