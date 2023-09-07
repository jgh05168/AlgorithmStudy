dir_dict = {'N': [-1, 0], 'W': [0, -1], 'S': [1, 0], 'E': [0, 1]}
dir_list = ['N', 'E', 'S', 'W']
# 북 동 남 서
# R : 정방향, L : 역방향


A, B = map(int, input().split())        # 땅 크기
N, M = map(int, input().split())        # 로봇, 명령

grid = [[0] * A for _ in range(B)]

robots = []
for i in range(1, N + 1):
    x, y, dir = input().split()
    grid[B - int(y)][int(x) - 1] = [i, dir]
    robots.append([i, int(x) - 1, B - int(y)])       # [robot_num, x(col), y(row)]

orders = []
for _ in range(M):
    robot, order, time = input().split()
    orders.append((int(robot), order, int(time)))


while orders:
    robots.sort(key=lambda x: x[0])
    robot, order, time = orders.pop(0)
    another_robot = 0
    row, col = robots[robot - 1][2], robots[robot - 1][1]
    crash_wall, crash_robot = False, False


    cur_dir = grid[row][col][1]
    # F일 경우
    if order == 'F':
        for _ in range(time):
            nrow, ncol = row + dir_dict[cur_dir][0], col + dir_dict[cur_dir][1]
            # 벽에 충돌할 경우
            if (nrow < 0 or nrow >= B) or (ncol < 0 or ncol >= A):
                crash_wall = True
                break
            # 로봇이랑 충돌할 경우
            elif grid[nrow][ncol] != 0:
                crash_robot = True
                another_robot = grid[nrow][ncol][0]
                break
            else:
                grid[nrow][ncol] = grid[row][col]
                grid[row][col] = 0
                robots[robot - 1][2], robots[robot - 1][1] = nrow, ncol
                row, col = nrow, ncol

    else:
        for idx, d in enumerate(dir_list):
            if d == cur_dir:
                cur_idx = idx
                break

        # R일 경우
        if order == 'R':
            for _ in range(time):
                cur_idx = (cur_idx + 1) % len(dir_list)
            grid[row][col][1] = dir_list[cur_idx]
        # L일 경우
        if order == 'L':
            for _ in range(time):
                cur_idx = (cur_idx - 1) % len(dir_list)
            grid[row][col][1] = dir_list[cur_idx]

    if crash_wall or crash_robot:
        break

if crash_wall:
    print(f'Robot {robot} crashes into the wall')
elif crash_robot:
    print(f'Robot {robot} crashes into robot {another_robot}')
else:
    print('OK')