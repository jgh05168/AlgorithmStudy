T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    drow = [0, 1, 1, 1, 0, -1, -1, -1]
    dcol = [1, 1, 0, -1, -1, -1, 0, 1]

    total_max = 0
    for row in range(N):
        for col in range(N):
            plussum, crosssum = arr[row][col], arr[row][col]
            for power in range(1, M):
                for k in range(len(drow)):
                    if k % 2 == 0:
                        nrow = row + drow[k] * power
                        ncol = col + dcol[k] * power
                        if 0 <= nrow and N > nrow and 0 <= ncol and N > ncol:
                            plussum += arr[nrow][ncol]
                    elif k % 2 == 1:
                        nrow = row + drow[k] * power
                        ncol = col + dcol[k] * power
                        if 0 <= nrow and N > nrow and 0 <= ncol and N > ncol:
                            crosssum += arr[nrow][ncol]

            if crosssum < plussum:
                if total_max < plussum:
                    total_max = plussum
            elif crosssum > plussum:
                if total_max < crosssum:
                    total_max = crosssum
            else:
                if total_max < crosssum:
                    total_max = crosssum

    print(f'#{tc} {total_max}')