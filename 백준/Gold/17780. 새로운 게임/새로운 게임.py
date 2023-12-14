import sys

# _, 오른, 왼, 위, 아래
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 보드 크기, 말 개수
N, K = map(int, sys.stdin.readline().rstrip().split())
# 0: 흰, 1: 빨, 2: 파 -> 기록한 보드
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 말 위치 기록(겹쳐진 말 포함)
record = [[[] for _ in range(N)] for _ in range(N)]

# 말 번호 별 위치, 방향 기록할 배열
horses_info = [[] for _ in range(K + 1)]
for i in range(1, K + 1):
    r, c, direction = map(int, sys.stdin.readline().rstrip().split())
    # 말 번호, 행, 열, 방향
    horses_info[i] = [i, r - 1, c - 1, direction]
    # 말 위치 기록(겹쳐지게)
    record[r - 1][c - 1].append(i)


# 가장 밑에 있는 말인지 확인하는 함수 (이동시키려는 말이 가장 밑에 있어야 이동시킬 수 있음)
def is_bottom_horse(h_num, x, y):
    horse_state = record[x][y]
    if horse_state[0] == h_num:
        return True
    else:
        return False


# 방향 반대로 바꾸는 함수
def reverse_dir(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    elif direction == 4:
        return 3


# 파란색이거나 벗어난 칸이라서 반대로 이동해봤는데 또 그런 상태인지 확인하는 함수
def is_blue_again(x, y, direction):
    rev_dir = reverse_dir(direction)
    nnx = x + dx[rev_dir]
    nny = y + dy[rev_dir]

    if nnx < 0 or nny < 0 or nnx >= N or nny >= N or board[nnx][nny] == 2:
        return True
    return False


# 다음 칸으로 이동시키는 함수
def move_next_pos(x, y, direction):
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 다음 칸이 판을 벗어나는 경우 or 파란칸
    if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] == 2:
        # 또 벗어나거나 파란칸이면 이동 안하고 방향만 반대로
        if is_blue_again(x, y, direction):
            return x, y, reverse_dir(direction)
        else:
            rev_dir = reverse_dir(direction)
            # 방향 바꿔서 이동한 칸의 색깔 별로 다시 처리해주기 위해 현재 함수 재귀 호출
            return move_next_pos(x, y, rev_dir)

    # 다음 칸이 빨강칸
    elif board[nx][ny] == 1:
        # 말 반대로 바꿔줌
        rev_horses = record[x][y][::-1]
        # 말들 차례로 다음 칸에 올림
        for value in rev_horses:
            record[nx][ny].append(value)
            # 말들 정보 갱신
            h_n, x, y, d = horses_info[value]
            horses_info[value] = [h_n, nx, ny, d]
        # 이전 칸에 있던 말을 모두 옮겼으므로 빈 칸으로 만들어 줌
        record[x][y] = []
    # 다음 칸이 흰칸
    elif board[nx][ny] == 0:
        # 말들 차례로 다음 칸에 올림
        for value in record[x][y]:
            record[nx][ny].append(value)
            # 말들 정보 갱신
            h_n, x, y, d = horses_info[value]
            horses_info[value] = [h_n, nx, ny, d]
        # 이전 칸에 있던 말을 모두 옮겼으므로 빈 칸으로 만들어 줌
        record[x][y] = []

    return nx, ny, direction


# 현재 턴에 모든 말들 이동시키는 함수
def move_all_horses():
    for horse in range(1, K + 1):
        horse_num, r, c, direction = horses_info[horse]
        # 말이 가장 밑이 아니면 다음 말로 넘어감
        if not is_bottom_horse(horse_num, r, c):
            continue

        # 현재 말 기준으로 옮기기 수행
        nx, ny, n_dir = move_next_pos(r, c, direction)
        # 현재 말 정보 갱신
        horses_info[horse_num] = [horse_num, nx, ny, n_dir]


# 게임이 끝날 수 있는지 확인하는 함수
def is_finish():
    for i in range(N):
        for j in range(N):
            if len(record[i][j]) >= 4:
                return True
    return False


# 게임 수행
answer = -1
time = 1
while time <= 1000:
    move_all_horses()

    if is_finish():
        answer = time
        break

    time += 1

print(answer)