import sys
input = sys.stdin.readline

dir_dict = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
rev_dir = {'D': 'U', 'U': 'D', 'L': 'R', 'R': 'L'}

def dfs(brow, bcol, row, col):
    global safe_zone
    # 종료조건
    if visited[row][col]:
        if (row, col) == (srow, scol):
            safe_zone += 1
        elif rev_dir[grid[row][col]] == grid[brow][bcol]:
            safe_zone += 1
        elif visited[row][col] == subset:
            safe_zone += 1
        return

    visited[row][col] = subset
    nrow, ncol = row + dir_dict[grid[row][col]][0], col + dir_dict[grid[row][col]][1]
    if 0 <= nrow < n and 0 <= ncol < m:
        dfs(row, col, nrow, ncol)




n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
safe_zone = 0
subset = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]:   # safe zone으로 가는 길이 이미 존재함.
            continue
        subset += 1
        srow, scol = i, j
        dfs(i, j, i, j)

print(safe_zone)