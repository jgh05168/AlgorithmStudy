'''
소용돌이로 이동한다.
상어 위치 : (N + 1) / 2, (N + 1) / 2)
이동방향 : 좌 하 우 상

방향을 나타내는 값 : 1 - 상 / 2 - 하 / 3 - 좌 / 4 - 우

1. 블리자드 시전
2. 빈 칸을 땡겨주기
3. 빈 칸 땡겨주면서 같은 값들이 4개 이상 연속하는지 cnt. 연속한다면 폭발 후 처음부터 다시 떙겨주기

구슬이 변화하는 단계.
A : 그룹에 들어있는 구슬의 개수
B : 그룹을 이루고 있는 구슬의 번호
# 칸에 들어가지 못하는 경우 구슬 삭제

정답 : 1 * 폭발한 1번 구슬 개수 + 2 * 폭발한 2번 구슬 개수 + 3 * 폭발한 3번 구슬 개수

시뮬레이션
'''

import sys
input = sys.stdin.readline

#    좌  하  우  상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# 마법 dict
dir_d = {1: 3, 2: 1, 3: 0, 4: 2}

def blizzard(shark_row, shark_col, dir, power):
    first, second, third = 0, 0, 0
    drow, dcol = dr[dir_d[dir]], dc[dir_d[dir]]
    for p in range(1, power + 1):
        row, col = shark_row + drow * p, shark_col + dcol * p
        grid[row][col] = -1     # 파괴 부분 -1로 값 설정


def change_dir(nrow, ncol, direction, start, end, high, low):
    # 좌측 끝일 경우
    if direction == 0 and ncol == start:
        direction = (direction + 1) % 4
        start -= 1
    # 아래 끝일 경우
    elif direction == 1 and nrow == low:
        direction = (direction + 1) % 4
        low += 1
    # 우측 끝일 경우
    elif direction == 2 and ncol == end:
        direction = (direction + 1) % 4
        end += 1
    # 위 끝일 경우
    elif direction == 3 and nrow == high:
        direction = (direction + 1) % 4
        high -= 1

    return direction, start, end, high, low


def move_marble(nrow, ncol, direction, start, end, high, low):
    # 앞으로 한 칸씩 다 땡겨주기
    direction, start, end, high, low = change_dir(nrow, ncol, direction, start, end, high, low)
    crow, ccol = nrow + dr[direction], ncol + dc[direction]

    while 0 <= crow < N and 0 <= ccol < N and grid[crow][ccol] != 0:
        grid[nrow][ncol] = grid[crow][ccol]     # 값 이동
        grid[crow][ccol] = 0
        nrow, ncol = crow, ccol

        direction, start, end, high, low = change_dir(nrow, ncol, direction, start, end, high, low)
        crow, ccol = nrow + dr[direction], ncol + dc[direction]
    if 0 <= crow < N and 0 <= ccol < N:
        grid[nrow][ncol] = grid[crow][ccol]     # 마지막값 옮겨주기


def slide():
    start, end, high, low = N // 2 - 1, N // 2 + 1, N // 2 - 1, N // 2 + 1
    row, col = N // 2, N // 2     # 상어 위치
    direction = 0
    # 이동하면서 같이 업데이트 해주어야 한다.
    # 끝에 도달할 때까지 반복
    while 0 <= row < N and 0 <= col < N and grid[row][col] != 0:
        nrow, ncol = row + dr[direction], col + dc[direction]

        # 파괴된 부분이거나 터졌을 경우 앞으로 전체 땡겨주기
        if grid[nrow][ncol] == -1:
            move_marble(nrow, ncol, direction, start, end, high, low)
        else:
            # 위치 땡겨주기
            direction, start, end, high, low = change_dir(nrow, ncol, direction, start, end, high, low)
            row, col = nrow, ncol

def check_same(marble, nrow, ncol, sdirection, start, end, high, low):
    global point
    global isbomb
    direction = sdirection
    direction, start, end, high, low = change_dir(nrow, ncol, direction, start, end, high, low)
    crow, ccol = nrow + dr[direction], ncol + dc[direction]

    count = 1
    stack = [(nrow, ncol)]
    # 구슬의 색이 같지 않을때까지 반복
    while 0 <= crow < N and 0 <= ccol < N and marble == grid[crow][ccol]:
        stack.append((crow, ccol))
        count += 1
        direction, start, end, high, low = change_dir(crow, ccol, direction, start, end, high, low)
        crow, ccol = crow + dr[direction], ccol + dc[direction]

    if count > 3:
        point += marble * count
        for drow, dcol in stack:
            grid[drow][dcol] = -1
        isbomb = True


def bomb():
    start, end, high, low = N // 2 - 1, N // 2 + 1, N // 2 - 1, N // 2 + 1
    row, col = N // 2, N // 2  # 상어 위치
    direction = 0
    # 이동하면서 같이 업데이트 해주어야 한다.
    # 끝에 도달할 때까지 반복
    row, col = row + dr[direction], col + dc[direction]
    while 0 <= row < N and 0 <= col < N and grid[row][col] != 0:
        # 이미 터진 부분은 건너뛴다
        if grid[row][col] == -1:
            # 위치 땡겨주기
            direction, start, end, high, low = change_dir(row, col, direction, start, end, high, low)
            row, col = row + dr[direction], col + dc[direction]
            continue

        # 다음 구슬이 같은지 같지 않은지 확인하고 있다면 폭발 진해
        check_same(grid[row][col], row, col, direction, start, end, high, low)

        # 위치 땡겨주기
        direction, start, end, high, low = change_dir(row, col, direction, start, end, high, low)
        row, col = row + dr[direction], col + dc[direction]


def count_marble(marble, row, col, sdirection, sstart, send, shigh, slow):
    direction = sdirection
    start, end, high, low = sstart, send, shigh, slow
    direction, start, end, high, low = change_dir(row, col, direction, start, end, high, low)
    crow, ccol = row + dr[direction], col + dc[direction]

    count = 1
    while 0 <= crow < N and 0 <= ccol < N and marble == grid[crow][ccol]:
        count += 1
        direction, start, end, high, low = change_dir(crow, ccol, direction, start, end, high, low)
        crow, ccol = crow + dr[direction], ccol + dc[direction]

    if count == 1:
        return row, col, sdirection, sstart, send, shigh, slow, count, marble
    else:
        return crow, ccol, direction, start, end, high, low, count, marble

def devide():
    global grid
    start, end, high, low = N // 2 - 1, N // 2 + 1, N // 2 - 1, N // 2 + 1
    row, col = N // 2, N // 2  # 상어 위치
    direction = 0
    new_grid = [[0] * N for _ in range(N)]
    new_grid[row][col] = 4

    # 두가지로 나누어서 생각해야 한다.
    ori_row, ori_col = row + dr[direction], col + dc[direction]
    ori_direction = 0
    ostart, oend, ohigh, olow = N // 2 - 1, N // 2 + 1, N // 2 - 1, N // 2 + 1
    marble_cnt = 2
    row, col = row + dr[direction], col + dc[direction]
    while 0 <= ori_row < N and 0 <= ori_col < N and marble_cnt < N * N and grid[ori_row][ori_col]:
        # 구슬 세기
        ori_row, ori_col, ori_direction, ostart, oend, ohigh, olow, cnt, marble = count_marble(grid[ori_row][ori_col], ori_row, ori_col, ori_direction, ostart, oend, ohigh, olow)

        # 업데이트
        # A : 구슬의 개수, B : 구슬의 번호
        # A
        new_grid[row][col] = cnt
        direction, start, end, high, low = change_dir(row, col, direction, start, end, high, low)
        row, col = row + dr[direction], col + dc[direction]
        # B
        new_grid[row][col] = marble
        direction, start, end, high, low = change_dir(row, col, direction, start, end, high, low)
        row, col = row + dr[direction], col + dc[direction]

        # 좌표의 변화가 없을 때만 원래의 좌표 위치 땡겨주기
        if cnt == 1:
            ori_direction, ostart, oend, ohigh, olow = change_dir(ori_row, ori_col, ori_direction, ostart, oend, ohigh, olow)
            ori_row, ori_col = ori_row + dr[ori_direction], ori_col + dc[ori_direction]

        marble_cnt += 2

    grid = new_grid

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

grid[N // 2][N // 2] = 4        # 상어를 4 변수로 설정
point = 0   # output
# 블리자드 마법 반복하기
for _ in range(M):
    d, s = map(int, input().split())

    # 블리자드 마법 시전
    blizzard(N // 2, N // 2, d, s)

    # 이동하면서 폭발한 값 업데이트
    slide()

    # 연쇄반응 끝날때까지 폭발시키기
    isbomb = True
    while isbomb:
        isbomb = False
        bomb()
        slide()

    # 구슬이 변화하는 단계 - 새로운 배열을 만들어서 copy해야 한다.
    devide()

print(point)