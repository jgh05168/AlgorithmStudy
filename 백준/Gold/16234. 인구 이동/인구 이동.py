dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    queue = []
    queue.append((srow, scol))
    country_loc = []
    country_loc.append((srow, scol))
    visited[srow][scol] = True
    population = 0
    check = False

    while queue:
        row, col = queue.pop(0)
        population += countries[row][col]
        for d in range(len(dr)):
            nrow = row + dr[d]
            ncol = col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and L <= abs(countries[row][col] - countries[nrow][ncol]) <= R and visited[nrow][ncol] == False:
                check = True
                queue.append((nrow, ncol))
                country_loc.append((nrow, ncol))
                visited[nrow][ncol] = True

    if check:
        avg_population = population // len(country_loc)
        for row, col in country_loc:
            countries[row][col] = avg_population
        return 1
    else:
        return 0

N, L, R = map(int, input().split())

countries = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[False] * N for _ in range(N)]
    vis = False

    for row in range(N):
        for col in range(N):
            if visited[row][col] == False:
                # for i in range(N):
                #     print(*countries[i])
                # print(cnt)
                check = bfs(row, col)
                if check == 1:
                    vis = True

    if vis == True:
        cnt += 1
    else:
        break

print(cnt)