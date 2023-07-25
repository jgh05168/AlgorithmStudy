T = int(input())

#       상 우 하 좌
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]


for test_case in range(1, T+1):
    N = int(input())

    # 3 2 2 1 1
    # 4 3 3 2 2 1 1
    # 5 4 4 3 3 2 2 1 1
    snail = [[0] * N for _ in range(N)]
    idxnumb = 0
    row, col = 0, 0

    for cnt in range(1, N**2 + 1):
        snail[row][col] = cnt
        row += drow[idxnumb]
        col += dcol[idxnumb]

        if row < 0 or col < 0 or row >= N or col >= N or snail[row][col] != 0:
            # 이전 index로 돌아가는 과정
            row -= drow[idxnumb]
            col -= dcol[idxnumb]

            # 방향전환 시켜주기 위한 코드
            idxnumb = (idxnumb + 1) % 4
            row += drow[idxnumb]
            col += dcol[idxnumb]


    print(f"#{test_case}")
    for i in range(0, N):
        print(*snail[i])