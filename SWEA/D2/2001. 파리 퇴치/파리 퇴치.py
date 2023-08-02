T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for row in range(N):
        for col in range(N):
            s = 0
            for catchrow in range(M):
                for catchcol in range(M):
                    nrow = row + catchrow
                    ncol = col + catchcol
                    if 0 <= nrow and N > nrow and 0 <= ncol and N > ncol:
                        s += arr[nrow][ncol]
            if max_v < s:
                max_v = s

    print(f'#{tc} {max_v}')

