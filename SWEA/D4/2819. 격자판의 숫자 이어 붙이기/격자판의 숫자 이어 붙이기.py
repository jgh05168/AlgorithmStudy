dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(row, col, number):
    if len(number) == 7:
        if number not in numbers:
            numbers.add(number)
        return
    else:
        for d in range(len(dr)):
            nrow = row + dr[d]
            ncol = col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N:
                dfs(nrow, ncol, number + grid[nrow][ncol])


T = int(input())

for tc in range(1, T + 1):
    numbers = set()
    N = 4
    grid = [list(input().split()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dfs(i, j, grid[i][j])

    print(f'#{tc} {len(numbers)}')
