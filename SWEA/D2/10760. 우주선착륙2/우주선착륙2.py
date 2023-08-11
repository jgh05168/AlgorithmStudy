T = int(input())

drow = [0, 1, 1, 1, 0, -1, -1, -1]
dcol = [1, 1, 0, -1, -1, -1, 0, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    mars_surf = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for row in range(N):
        for col in range(M):
            landing_point = mars_surf[row][col]
            landing_count = 0
            for d in range(8):
                nrow, ncol = row + drow[d], col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < M:
                    if mars_surf[nrow][ncol] < landing_point:
                        landing_count += 1
            if landing_count >= 4:
                cnt += 1

    print(f'#{tc} {cnt}')