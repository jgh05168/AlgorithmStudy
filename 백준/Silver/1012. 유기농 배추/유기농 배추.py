import sys
sys.setrecursionlimit(10**6)

T = int(input())

drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]


def dfs(visited, field, row, col):
    if visited[row][col] == True:
        return
    else:
        visited[row][col] = True
        for d in range(len(drow)):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if 0 <= nrow < N and 0 <= ncol < M and field[nrow][ncol] == 1 and visited[nrow][ncol] == False:
                dfs(visited, field, nrow, ncol)



for tc in range(1, T + 1):
    cnt = 0
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        col, row = map(int, input().split())
        field[row][col] = 1

    for row in range(N):
        for col in range(M):
            if field[row][col] == 1 and visited[row][col] == False:
                dfs(visited, field, row, col)
                cnt += 1

    print(cnt)