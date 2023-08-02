test_case = 0

while test_case <= 10:
    N = 100
    test_case = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    total = 0
    totalinv = 0
    for i in range(N):
        totalrow = 0
        totalcol = 0
        for j in range(N):
            totalrow += arr[i][j]
            totalcol += arr[j][i]
        if max_v < totalrow:
            max_v = totalrow
        if max_v < totalcol:
            max_v = totalcol


        total += arr[i][i]
        totalinv += arr[i][N - i - 1]
        if max_v < total:
            max_v = total
        if max_v < totalinv:
            max_v = totalinv


    print(f'#{test_case} {max_v}')

    if test_case == 10:
        exit()