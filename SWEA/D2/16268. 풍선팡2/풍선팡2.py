T = int(input())

for tc in range(1, T+1):

    N, M = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    drow = [0, 1, 0, -1]
    dcol = [1, 0, -1, 0]

    for row in range(N):
        for col in range(M):
            s = arr[row][col]
            for k in range(len(drow)):
                nrow = row + drow[k]
                ncol = col + dcol[k]
                if 0 <= nrow and N > nrow and 0 <= ncol and M > ncol:
                    s += arr[nrow][ncol]
            if max_value < s:
                max_value = s

    print(f'#{tc} {max_value}')