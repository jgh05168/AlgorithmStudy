for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    # column 별로 탐색
    cnt = 0
    for col in range(N):
        check = False
        for row in range(N):
            # 위에서부터 탐색해서 만약 N극을 가진 칸이 있다면
            if table[row][col] == 1:
                check = True        # 가려는 쪽이 있다고 판단
            # 만약 S극을 가진 칸을 만났고, 현재 칸 이전에 N극을 가진 칸이 존재한다면
            elif table[row][col] == 2 and check:
                cnt += 1    # 이동불가하므로, 맞닿아있는 면 + 1
                check = False

    print(f'#{tc} {cnt}')