'''
대각선 방향으로 움직이고, 사각형 모양을 그려야 한다.

제약사항
1. 카페 투어 중 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안된다.
2. 사각형 모양을 무조건 그려야 한다.
3. 왔던 길을 되돌아가면 안된다.

- 돌 수 있는 경우를 한 변에 대해서 계산한 다음 재귀로 넘겨주는 방식
- dfs + 백트래킹
정답 : 가장 많이 먹을 수 있는 카페 메뉴의 개수

10 * 20 * 20 * 40 < 20000000
'''


#    5  7  11  1
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def recur(path, row, col, startidx, menus, menu_cnt):
    global max_v
    global max_yum
    if path == 4:
        return

    temp = 0
    menu_temp = []
    while 0 <= row < N and 0 <= col < N:
        nrow, ncol = row + dr[path], col + dc[path]
        if 0 <= nrow < N and 0 <= ncol < N and cafe_map[nrow][ncol] not in menus and cafe_map[nrow][ncol] not in menu_temp:
            temp += 1
            menu_temp.append(cafe_map[nrow][ncol])
            recur(path + 1, nrow, ncol, startidx, menus + menu_temp, menu_cnt + temp)
            row, col = nrow, ncol
        else:
            if (row + dr[path], col + dc[path]) == startidx and len(menus) > 3:
                if max_v < menu_cnt + temp:
                    max_v = menu_cnt + temp
            return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cafe_map = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    max_yum = 0
    # 한번씩 모두 돌아본다.
    for row in range(N):
        for col in range(1, N - 1):
            if (row, col) == (0, 0) or (row, col) == (N - 1, 0) or (row, col) == (0, N - 1) or (row, col) == (N - 1, N - 1):
                continue
            recur(0, row, col, (row, col), [cafe_map[row][col]], 1)

    if not max_v:
        max_v = -1
    print(f'#{tc} {max_v}')