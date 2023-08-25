dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)

else:
    # 시작 인덱스
    row, col = R - 1, 0

    sitmap = [[0] * C for _ in range(R)]
    sitmap[row][col] = 1        # 시작인덱스는 1로 시작
    change = 0
    if K == 1:
        print(1, 1)
    else:
        for i in range(2, C * R + 1):
            nrow = row + dr[change]
            ncol = col + dc[change]

            if nrow < 0 or nrow >= R or ncol < 0 or ncol >= C or sitmap[nrow][ncol] != 0:
                change = (change + 1) % 4       # 4방향이기 때문에 인덱스 넘버를 조절하기 위한 용도
                nrow = row + dr[change]
                ncol = col + dc[change]

            row, col = nrow, ncol
            sitmap[row][col] = i
            if i == K:
                print(col + 1, R - row)

