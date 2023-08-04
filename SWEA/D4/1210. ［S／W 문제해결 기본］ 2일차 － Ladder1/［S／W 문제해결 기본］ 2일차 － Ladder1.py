for t in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]


    row = len(ladder) - 1

    # 도착 인덱스 찾기
    for i in range(len(ladder)):
        if ladder[row][i] == 2:
            col = i
            break

    # 미로찾기 같은 문제의 경우 왔던 길을 [0]으로 처리하는 방법이 유용

    # 사다리타기 게임의 규칙
    # 상하 방향으로 가는데 중간 좌우 방향에 길이 있다면 좌우로 우선 이동
    #    좌  우  상
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    while row > 0:
        for dir in range(3):
            nrow = row + dr[dir]
            ncol = col + dc[dir]

            if 0 <= nrow < len(ladder) and 0 <= ncol < len(ladder) and ladder[nrow][ncol] == 1:
                row = nrow
                col = ncol
                # 왔던 길을 다시 보지 않도록 [0]으로 변경
                ladder[row][col] = 0
                break

    # 반복문이 끝난다면 r = 0

    print(f'#{tc} {col}')



