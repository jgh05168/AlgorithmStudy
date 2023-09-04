import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
ds = [1, -1]
def bfs(sstair, srow, scol):
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    queue = [(sstair, srow, scol)]
    visited[sstair][srow][scol] = 0

    while queue:
        stair, row, col = queue.pop(0)
        # 동서남북
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < R and 0 <= ncol < C and visited[stair][nrow][ncol] == -1 and building[stair][nrow][ncol] != '#':
                visited[stair][nrow][ncol] = visited[stair][row][col] + 1
                if building[stair][nrow][ncol] == 'E':
                    return visited[stair][nrow][ncol]
                queue.append((stair, nrow, ncol))

        # 상하
        for s in range(len(ds)):
            nstair = stair + ds[s]
            if 0 <= nstair < L and visited[nstair][row][col] == -1 and building[nstair][row][col] != '#':
                visited[nstair][row][col] = visited[stair][row][col] + 1
                if building[nstair][row][col] == 'E':
                    return visited[nstair][row][col]
                queue.append((nstair, row, col))

    return 0

while True:
    L, R, C = map(int, input().split())     # L : 층 수 R, C : 행, 열
    if L == 0 and R == 0 and C == 0:
        break
    building = [[] for _ in range(L)]  # 각 층 정보 주어짐
    for i in range(L):
        building[i] = [input() for _ in range(R)]
        input()

    min = 0
    find = False
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    min = bfs(i, j, k)
                    find = True
                    break
            if find:
                break
        if find:
            break

    if not min:
        print('Trapped!')
    else:
        print(f'Escaped in {min} minute(s).')
