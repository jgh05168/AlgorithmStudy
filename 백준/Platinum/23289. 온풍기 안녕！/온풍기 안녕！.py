'''
온풍기 설치

1. 집에 있는 온풍기에서 바람이 한 번 나온다.
2. 온도가 조절된다
3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
4. 조사하는 모든 칸의 온도가 k 이상이 되었는지 검사. 아니면 다시 시작

온풍기는 상하좌우 중 하나에서 나옴. 바람은 옆위, 옆, 옆아래 (x-1, y+1), (x, y+1), (x+1, y+1) 로 뻗어나간다.
    - 체크해봐야 할 사항(오른쪽 기준)
        1. 옆 위로 바람이 갈 수 있는 경우는 (x, y)와 (x-1, y) /  (x-1, y)와 (x-1, y+1) 모두 벽이 없어야 한다.
        2. 옆으로 갈 수 있는 경우는  (x, y)와 (x, y+1) 에 벽이 없어야 한다.
        3. 옆아래로 갈 수 있는 경우는  (x, y)와 (x+1, y), (x+1, y)와 (x+1, y+1) 사이에 벽이 없어야 한다.

온풍기가 2대 이상인 경우 각각의 온풍기에 의해서 상승한 온도를 모두 합한 값이 해당 칸의 상승한 온도이다.

온도가 조절되는 과정 :
모든 인접한 칸에서 온도가 높은 칸에서 낮은 칸으로 (두 칸의 온도의 차이 // 4)만큼 온도가 조절된다.
온도가 높은 칸은 이 값만큼 온도가 감소하고, 낮은 칸은 온도가 상승한다.
벽이 있는 경우에는 온도가 조절되지 않는다.
모든 칸에 대해서 동시에 발생한다.

-> 새로운 tmp 배열 생성. 원래 값을 순회하면서 비교한다.
    위 계산식을 사용해서 인접 4방향에 대해 원래 값으로 계산
    visited 배열을 사용해서 이미 계산 완료되었는지 체크
    새로운 tmp 배열의 값 + 새로 계산된 값을 tmp 배열에 저장

'''

from collections import deque
import sys
input = sys.stdin.readline

#       오  왼  위  아
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

wind_d = [-1, 0, 1]

'''
0: 빈 칸
1: 방향이 오른쪽인 온풍기가 있음
2: 방향이 왼쪽인 온풍기가 있음
3: 방향이 위인 온풍기가 있음
4: 방향이 아래인 온풍기가 있음
5: 온도를 조사해야 하는 칸

t가 0인 경우 (x, y)와 (x-1, y) 사이에 벽이 있는 것이고, 1인 경우에는 (x, y)와 (x, y+1) 사이에 벽이 있는 것
'''

def check_blow(row, col, d, wind_path):
    try:
        # 현재 위치에서 3가지 방면에 대해서 조사해야한다.
        # 오른쪽
        if d == 1:
            if wind_path == 0:
                # 둘 중 한군데라도 막혀있다면 불가능
                if walls_map[2][row][col] or walls_map[0][row - 1][col]:
                    return False
            elif wind_path == 1:
                if walls_map[0][row][col]:
                    return False
            else:
                if walls_map[3][row][col] or walls_map[0][row + 1][col]:
                    return False

        # 왼쪽
        elif d == 2:
            if wind_path == 0:
                # 둘 중 한군데라도 막혀있다면 불가능
                if walls_map[2][row][col] or walls_map[1][row - 1][col]:
                    return False
            elif wind_path == 1:
                if walls_map[1][row][col]:
                    return False
            else:
                if walls_map[3][row][col] or walls_map[1][row + 1][col]:
                    return False

        # 위쪽
        elif d == 3:
            if wind_path == 0:
                # 둘 중 한군데라도 막혀있다면 불가능
                if walls_map[1][row][col] or walls_map[2][row][col - 1]:
                    return False
            elif wind_path == 1:
                if walls_map[2][row][col]:
                    return False
            else:
                if walls_map[0][row][col] or walls_map[2][row][col + 1]:
                    return False
        # 아래쪽
        else:
            if wind_path == 0:
                # 둘 중 한군데라도 막혀있다면 불가능
                if walls_map[1][row][col] or walls_map[3][row][col - 1]:
                    return False
            elif wind_path == 1:
                if walls_map[3][row][col]:
                    return False
            else:
                if walls_map[0][row][col] or walls_map[3][row][col + 1]:
                    return False
        return True

    except:
        return False

def heat(heater):
    visited_wind = [[0] * C for _ in range(R)]
    d = heater[2]
    srow, scol = heater[0] + dr[d], heater[1] + dc[d]
    visited_wind[srow][scol] = 1
    queue = deque()
    queue.append((srow, scol, 5))

    while queue:
        row, col, power = queue.popleft()

        room[row][col] += power

        for wind in range(len(wind_d)):
            # 상하, 좌우 일 경우 배열인덱스가 달라진다.
            # 벽에 막혀있는지 확인
            # 3가지 경우에 대해서 각각 확인
            if not check_blow(row, col, d, wind):
                continue

            if d in (1, 2):
                nrow, ncol = row + dr[d] + wind_d[wind], col + dc[d]
            else:
                nrow, ncol = row + dr[d], col + dc[d] + wind_d[wind]

            if 0 <= nrow < R and 0 <= ncol < C and not visited_wind[nrow][ncol] and power > 1:
                visited_wind[nrow][ncol] = 1
                queue.append((nrow, ncol, power - 1))


def conduction():
    global room
    temp_room = [[0] * C for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    for row in range(R):
        for col in range(C):
            if not temp_room[row][col]:
                base_temp = room[row][col]
            else:
                base_temp = temp_room[row][col]
            visited[row][col] = 1
            for d in range(1, len(dr)):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 <= nrow < R and 0 <= ncol < C and not visited[nrow][ncol]:
                    # 벽으로 막혀있다면 continue
                    if not check_blow(row, col, d, 1):
                        continue
                    # 새로운 곳이 이미 바뀐 온도가 있는지 체크
                    if not temp_room[nrow][ncol]:
                        another_temp = room[nrow][ncol]
                    else:
                        another_temp = temp_room[nrow][ncol]
                    # 인접한 곳의 온도가 현재보다 더 크다면 조절
                    grad_temp = abs(room[row][col] - room[nrow][ncol]) // 4
                    if room[row][col] < room[nrow][ncol]:
                        base_temp += grad_temp
                        # 새로운 곳에는 다시 들어가지 않는다.
                        if another_temp - grad_temp < 0:
                            temp_room[nrow][ncol] = 0
                        else:
                            temp_room[nrow][ncol] = another_temp - grad_temp
                    else:
                        base_temp -= grad_temp
                        if another_temp + grad_temp < 0:
                            temp_room[nrow][ncol] = 0
                        else:
                            temp_room[nrow][ncol] = another_temp + grad_temp

            if base_temp < 0:
                temp_room[row][col] = 0
            else:
                temp_room[row][col] = base_temp

    room = temp_room



R, C, K = map(int, input().split())
room_info = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
chocolates = 0
walls_map = [[[0] * C for _ in range(R)] for _ in range(4)]     # 0: 오 1: 왼 2: 위 3: 아
room = [[0] * C for _ in range(R)]
for _ in range(W):
    x, y, t = map(int, input().split())
    if not t:
        walls_map[2][x - 1][y - 1] = 1     # 북쪽 방면으로 벽이 있다.
        walls_map[3][x - 2][y - 1] = 1     # 남쪽 방면으로 벽이 있다.
    else:
        walls_map[0][x - 1][y - 1] = 1     # 오른쪽 방면으로 벽이 있다.
        walls_map[1][x - 1][y] = 1         # 왼쪽 방면으로 벽이 있다.

# 온풍기, 조사해야 할 위치 탐색
heaters = []
examine_loc = []
for i in range(R):
    for j in range(C):
        if room_info[i][j] > 0:      # 빈 칸이 아닌 경우에 대해서 조사
            if room_info[i][j] == 5:
                examine_loc.append((i, j))
            else:
                heaters.append((i, j, room_info[i][j]))


while chocolates <= 100:
    # 1. 온풍기에서 바람 뿜기
    for heater in heaters:
        heat(heater)

    # 2. 인접 칸에 대해서 온도 흩뿌리기
    conduction()

    # 3. 바깥 온도가 1 이상인 경우 1씩 감소
    for row in range(R):
        for col in range(C):
            if room[row][col] > 0:
                if row in (0, R - 1) or col in (0, C - 1):
                    room[row][col] -= 1

    # 4. 초콜렛 하나 먹기
    chocolates += 1

    # 5. 조사하는 모든 칸의 온도가 K 이상일 경우 테스트 종료
    check_cnt = 0
    for erow, ecol in examine_loc:
        if room[erow][ecol] >= K:
            check_cnt += 1
    if check_cnt == len(examine_loc):
        break

print(chocolates)