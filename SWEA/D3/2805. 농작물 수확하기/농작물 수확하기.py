T = int(input())
#      5시 7시 11시 1시     방향
drow = [1, 1, -1, -1]
dcol = [1, -1, -1, 1]

for tc in range(1, T + 1):
    N = int(input())

    harvest = [list(map(int, input())) for _ in range(N)]

    get_range = N // 2          # 중앙점 위치를 알기 위한 계산
    margin = harvest[get_range][get_range]  # 농작물의 가장 중앙값을 초기값으로

    # 안쪽부터 바깥쪽까지 대각선 방향으로 훓을 것이다.
    for k in range(1, get_range + 1):
        row, col = get_range - k, get_range     # 방향벡터를 다 돌았으면 row - 1을 해주어 한칸 위로 올린다.
        for d in range(4):             # 방향 벡터 설정
            for i in range(k):         # 얼만큼 대각선 방향으로 이동할 것인지 k번으로 설정
                nrow = row + drow[d]
                ncol = col + dcol[d]
                # print(nrow, ncol)
                if 0 <= nrow < N or 0 <= ncol < N:
                    row, col = nrow, ncol
                    margin += harvest[row][col]


    print(f'#{tc} {margin}')