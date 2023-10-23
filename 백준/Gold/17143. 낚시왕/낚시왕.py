'''
낚시왕이 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

1. 낚시왕이 오른쪽(column)으로 한 칸 이동
2. 낚시왕이 있는 열에 있는 상어 중에서 땅(row)과 제일 가까운 상어를 없앤다.
3. 상어 이동
    3-1. 방향바꿔가며 왔다갔다 반복. 이동해야하는 칸 수 주어짐
    3-2. 이동 후 같은 칸에 상어가 두 마리 이상 있는 경우 크기가 큰 상어가 나머지 상어를 잡아먹음

낚시왕이 잡은 상어 크기의 합 구하기

단순 구현, 시뮬
'''

from collections import deque
import sys, copy
input = sys.stdin.readline

change_dir = {1: 2, 2: 1, 3: 4, 4: 3}       # 상하 -> 하상, 좌우 -> 우좌
#       상  하  우  좌
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]


def get_shark(fisher_loc):
    global total_size, total_shark
    for row in range(R):
        if grid[row][fisher_loc] != 0:       # 지면과 가장 가까운 상어를 발견하면 잡은 뒤 반복문 종료
            # 잡은 상어 제거
            total_shark = list(set(total_shark).difference(set([(row, fisher_loc, grid[row][fisher_loc][0], grid[row][fisher_loc][1], grid[row][fisher_loc][2])])))
            total_size += grid[row][fisher_loc][2]
            grid[row][fisher_loc] = 0
            break


def move_shark(sharks):
    global total_shark, grid
    temp_grid = [[0] * C for _ in range(R)]
    eaten_list = []
    temp_total_sharks = deque(total_shark)
    for shark in range(sharks):
        grid[total_shark[shark][0]][total_shark[shark][1]] = 0        # 격자 내 상어 초기화
        row, col, speed, direction, size = temp_total_sharks.popleft()
        move = 0
        # 움직이기
        while move < speed:
            nrow, ncol = row + dr[direction], col + dc[direction]
            if 0 <= nrow < R and 0 <= ncol < C:
                row, col = nrow, ncol
            else:
                direction = change_dir[direction]
                row += dr[direction]
                col += dc[direction]
            move += 1

        # 먹혔는지 확인하기
        if not temp_grid[row][col]:
            temp_grid[row][col] = (speed, direction, size)
            temp_total_sharks.append((row, col, speed, direction, size))
        else:
            # 사이즈 확인
            if temp_grid[row][col][2] < size:
                eaten_list.append((row, col, temp_grid[row][col][0], temp_grid[row][col][1], temp_grid[row][col][2]))
                temp_grid[row][col] = (speed, direction, size)
                temp_total_sharks.append((row, col, speed, direction, size))
            else:
                eaten_list.append((row, col, speed, direction, size))

    grid = copy.deepcopy(temp_grid)
    total_shark = list(set(list(temp_total_sharks)).difference(set(eaten_list)))


R, C, M = map(int, input().split())
grid = [[0] * C for _ in range(R)]

total_shark = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    grid[r - 1][c - 1] = (s, d, z)
    total_shark.append((r - 1, c - 1, s, d, z))

total_size = 0
for fisher in range(C):     # 낚시왕이 C의 끝에 다다를 때까지 반복(다다르면 종료)
    # 지면과 가장 가까운 상어 잡기
    get_shark(fisher)

    # 상어 이동
    move_shark(len(total_shark))

print(total_size)
