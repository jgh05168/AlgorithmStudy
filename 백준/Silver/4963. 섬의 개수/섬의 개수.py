import sys
sys.setrecursionlimit(10**6)

drow = [0, 1, 1, 1, 0, -1, -1, -1]
dcol = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(row, col):
    if visited[row][col] == True:
        return
    else:
        visited[row][col] = True
        for d in range(len(drow)):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if 0 <= nrow < h and 0 <= ncol < w and land[nrow][ncol] == 1 and visited[nrow][ncol] == False:
                dfs(nrow, ncol)

w, h = map(int, input().split())
while w != 0 or h != 0:
    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    island = 0

    for row in range(h):
        for col in range(w):
            if land[row][col] == 1 and visited[row][col] == False:
                dfs(row, col)
                island += 1

    print(island)
    w, h = map(int, input().split())

