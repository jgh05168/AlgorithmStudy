T = int(input())

drow = [1, 1, -1, -1]
dcol = [1, -1, -1, 1]

for tc in range(1, T + 1):
    N = int(input())

    harvest = [list(map(int, input())) for _ in range(N)]

    get_range = N // 2
    margin = harvest[get_range][get_range]


    for k in range(1, get_range + 1):
        row, col = get_range - k, get_range
        for d in range(4):
            for i in range(k):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                # print(nrow, ncol)
                if 0 <= nrow < N or 0 <= ncol < N:
                    row, col = nrow, ncol
                    margin += harvest[row][col]


    print(f'#{tc} {margin}')