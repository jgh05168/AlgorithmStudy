'''
게임 순서

1. 종수의 아두이노를 이동
2. 종수의 아두이노가 미친아두이노가 있는 칸으로 이동할 경우 중간에 게임 종료
3. 미친 아두이노는 8가지 방향 중 종수와 가까워지는 방향으로 한 칸 이동한다.
    -> 8 방향에 대해 맨해튼 거리 계산. 이후 가까워 지는 방향으로 이동
4. 미친 아두이노가 종수의 아두이노가 있는 칸으로 이동한 경우 게임 종료
5. 두 대 이상의 미친아두이노가 같은 칸에 있는 경우 두 아두이노는 파괴된다.
'''


import sys
input = sys.stdin.readline

dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]


def move_jongsu(row, col, move):
    global jongsu
    nrow, ncol = row + dr[move], col + dc[move]
    if board[nrow][ncol] != 'R':
        board[row][col] = '.'
        board[nrow][ncol] = 'I'
        jongsu = [nrow, ncol]
        return True
    else:
        return False


def move_crazy_robots():
    global crazy_robots
    n = len(crazy_robots)
    visited = [[0] * C for _ in range(R)]
    tmp_list = []
    overlap_list = []
    for crobot in range(n):
        min_grid = (0, 0)
        min_d = int(1e9)
        row, col = crazy_robots[crobot]
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < R and 0 <= ncol < C:
                if (nrow, ncol) == (jongsu[0], jongsu[1]):      # 종수를 잡은 경우
                    return False
                if min_d > abs(jongsu[0] - nrow) + abs(jongsu[1] - ncol):
                    min_d = abs(jongsu[0] - nrow) + abs(jongsu[1] - ncol)
                    min_grid = (nrow, ncol)

        if not visited[crazy_robots[crobot][0]][crazy_robots[crobot][1]]:
            board[crazy_robots[crobot][0]][crazy_robots[crobot][1]] = '.'

        if visited[min_grid[0]][min_grid[1]]:
            board[min_grid[0]][min_grid[1]] = '.'
            overlap_list.append(min_grid)
        else:
            board[min_grid[0]][min_grid[1]] = 'R'
            visited[min_grid[0]][min_grid[1]] = 1
            tmp_list.append(min_grid)

    crazy_robots = list(set(tmp_list).difference(set(overlap_list)))

    return True


R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
moves = list(input().rstrip())

crazy_robots = []
jongsu = []
# 로봇들 위치 찾기
for i in range(R):
    for j in range(C):
        if board[i][j] == 'I':
            jongsu = [i, j]
        elif board[i][j] == 'R':
            crazy_robots.append((i, j))

for order in range(len(moves)):
    move = int(moves[order]) - 1

    # 1. 종수 아두이노 이동
    canMove = move_jongsu(jongsu[0], jongsu[1], move)
    if not canMove:
        print(f'kraj {order + 1}')
        break

    # 2. 미친 아두이노들 움직이기
    meetJongsu = move_crazy_robots()
    if not meetJongsu:
        print(f'kraj {order + 1}')
        break

else:
    for i in range(R):
        print(''.join(board[i]))
