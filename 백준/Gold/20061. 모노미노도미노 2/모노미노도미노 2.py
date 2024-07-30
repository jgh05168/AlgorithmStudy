'''
가로 : 2 * 4 + 2
세로 : 2 * 4 + 2
블록 모양 : ㅁ, ㅁㅁ, ㅁㅁ(세로)

- 빨간색 보드에 블록을 놓으면 초록, 파란 보드로 이동한다.
    - 경계를 만날 때까지 이동한다.
    - 초록 보드의 행 or 파란 보드의 열이 타일로 가득찬다면,
        - 타일은 모두 사라지고 사라진 행(열) 수만큼 이동한다.
        - 사라진 행(열) 마다 1점씩 획득
- 특별한 칸(n + 2) : 행(열)의 수만큼 이동한다.

풀이 순서:
1. 빨간색 보드에 블록을 놓고, 이동시킨다.
2. 행(열) 확인해가며 점수가 날 수 있는지 확인해본다
    2-1. 점수가 났다면 점수 체크
    2-2. gravity를 사용하여 사라진 행(열) 만큼 내리기
3. 특별한 칸 체크: 있다면 내리기

t = 1 : 1 x 1
t = 2 : 1 x (1 + 1)
t = 3 : (1 + 1) x 1
'''

import sys
input = sys.stdin.readline


def move_green(t, x, y):
    if t == 1:
        while x < 10:
            if board[x][y]:
                break
            x += 1
        board[x - 1][y] = 1
    elif t == 2:
        check_move = True
        ny = [y, y + 1]
        while x < 10:
            for i in range(2):
                if board[x][ny[i]]:
                    check_move = False
                    break
            else:
                x += 1
            if not check_move:
                break
        board[x - 1][ny[0]] = board[x - 1][ny[1]] = 1
    else:
        check_move = True
        nx = [x, x + 1]
        while nx[1] < 10:
            for i in range(2):
                if board[nx[i]][y]:
                    check_move = False
                    break
            else:
                nx[0], nx[1] = nx[0] + 1, nx[1] + 1
            if not check_move:
                break
        board[nx[0] - 1][y] = board[nx[1] - 1][y] = 1


def move_blue(t, x, y):
    if t == 1:
        while y < 10:
            if board[x][y]:
                break
            y += 1
        board[x][y - 1] = 1
    elif t == 2:
        check_move = True
        ny = [y, y + 1]
        while ny[1] < 10:
            for i in range(2):
                if board[x][ny[i]]:
                    check_move = False
                    break
            else:
                ny[0], ny[1] = ny[0] + 1, ny[1] + 1
            if not check_move:
                break
        board[x][ny[0] - 1] = board[x][ny[1] - 1] = 1
    else:
        check_move = True
        nx = [x, x + 1]
        while y < 10:
            for i in range(2):
                if board[nx[i]][y]:
                    check_move = False
                    break
            else:
                y += 1
            if not check_move:
                break
        board[nx[0]][y - 1] = board[nx[1]][y - 1] = 1


def check_point():
    global ans
    for color in range(2):      # 0 : green | 1 : blue
        if not color:
            # 행은 10 ~ 6, 열은 0 ~ 4
            for r in range(10 - 1, 5, -1):
                for c in range(4):
                    if not board[r][c]:
                        break
                else:
                    ans += 1
                    for c in range(4):
                        board[r][c] = 0
        else:
            # 행은 0 ~ 4, 열은 10 ~ 6
            for c in range(10 - 1, 5, -1):
                for r in range(4):
                    if not board[r][c]:
                        break
                else:
                    ans += 1
                    for r in range(4):
                        board[r][c] = 0


def gravity():
    for color in range(2):      # 0 : green | 1 : blue
        if not color:
            vanished = 0
            # 행은 10 ~ 6, 열은 0 ~ 4
            for r in range(10 - 1, 3, -1):
                for c in range(4):
                    if board[r][c]:
                        # 사라진 행의 수만큼 내리고 break
                        for nc in range(4):
                            board[r + vanished][nc] = board[r][nc]
                            if vanished:
                                board[r][nc] = 0
                        break
                else:
                    # 사라진 행의 수 + 1
                    vanished += 1

        else:
            # 행은 0 ~ 4, 열은 10 ~ 6
            vanished = 0
            for c in range(10 - 1, 3, -1):
                for r in range(4):
                    if board[r][c]:
                        for nr in range(4):
                            board[nr][c + vanished] = board[nr][c]
                            if vanished:
                                board[nr][c] = 0
                        break
                else:
                    # 사라진 열의 수 + 1
                    vanished += 1


def special():
    for color in range(2):      # 0 : green | 1 : blue
        if not color:
            cnt_special = 0
            if board[4].count(1):
                cnt_special += 1
            if board[5].count(1):
                cnt_special += 1
            # 센 칸 수 만큼 내리기
            if cnt_special:
                for r in range(10 - cnt_special - 1, 1, -1):
                    for c in range(4):
                        board[r + cnt_special][c] = board[r][c]

        else:
            cnt_special = 0
            tmp_cnt = [0, 0]
            for r in range(4):
                if board[r][4]:
                    tmp_cnt[0] += 1
                if board[r][5]:
                    tmp_cnt[1] += 1
            if tmp_cnt[0]:
                cnt_special += 1
            if tmp_cnt[1]:
                cnt_special += 1
            # 센 칸 수 만큼 내리기
            for c in range(10 - cnt_special - 1, 1, -1):
                for r in range(4):
                    board[r][c + cnt_special] = board[r][c]



n = int(input())
board = [[0] * 10 for _ in range(10)]
ans = 0
for _ in range(n):
    t, x, y = map(int, input().split())

    # 1. 빨간색 보드에 블록을 놓고(실제로 놓을 필요는 없음) 이동시키기
    move_green(t, x, y)
    move_blue(t, x, y)

    # 2-1. 행 / 열 확인해가며 완성되는 부분 있는지 체크
    check_point()

    # 2-2. 빈 행 열 파악해서 gravity 시키기
    gravity()

    # 3. 특별한 칸 체크 후 칸만큼 내리기
    special()

print(ans)
# 블럭 갯수 세기
cnt_block = 0
for i in range(10):
    cnt_block += sum(board[i])
print(cnt_block)