T = int(input())

#      우  하  좌  상
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    flowers = [list(map(int, input().split())) for _ in range(N)]

    max_pang = 0
    for row in range(N):
        for col in range(M):
            pang = flowers[row][col]
            for d in range(len(drow)):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < M:
                    pang += flowers[nrow][ncol]

            if max_pang < pang:
                max_pang = pang

    print(f'#{tc} {max_pang}')