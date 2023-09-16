'''
뱀게임

조건 1. 머리가 자기 몸이나 벽에 닿으면 게임 끝
조건 2. 사과를 먹으면 길이 늘어남(꼬리 위치 수정 해 줄 필요 x)
조건 3. 사과 안 먹으면(꼬리 위치 수정)

시뮬레이션 문제

- 방향전환(왼/오)에 대한 vector를 mod를 사용하여 표현

- 머리와 꼬리 위치를 기억하고 있어야 한다.
'''

from collections import deque
import sys
input = sys.stdin.readline

# 오른쪽부터 향한다
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# inputs
N = int(input())
board = [[-1] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1
L = int(input())

# 게임 시작
# -1 : 빈 칸
# 0 : snake
# 1 : apple
time = 0
row, col = 0, 0     # 시작 위치
board[row][col] = 0
dir = 0
end = True
snake = deque()
snake.append((row, col))

for _ in range(L):
    X, C = input().split()

    # 이동하기
    for t in range(1, int(X) - time + 1):
        nrow, ncol = row + dr[dir], col + dc[dir]

        # 벽에 닿거나 자기 몸에 닿은 경우
        if 0 > nrow or nrow >= N or 0 > ncol or ncol >= N or board[nrow][ncol] == 0:
            end = False
            break

        # 만약 이동한 칸에 사과가 있다면
        elif board[nrow][ncol] == 1:
            board[nrow][ncol] = 0
            snake.appendleft((nrow, ncol))
            row, col = nrow, ncol

        # 사과가 없다면
        else:
            board[nrow][ncol] = 0
            snake.appendleft((nrow, ncol))
            tail_row, tail_col = snake.pop()
            board[tail_row][tail_col] = -1
            row, col = nrow, ncol

    else:
        # for문에서 break당하지 않고 무사히 완료했다면
        # 방향 바꿔주기
        if C == 'L':    # 왼쪽으로 방향 전환
            dir = (dir - 1) % 4
        elif C == 'D':           # 오른쪽으로 방향 전환
            dir = (dir + 1) % 4

    time += t
    if not end:
        break


# 명령이 끝난 뒤
while end:
    # 이동하기

    nrow, ncol = row + dr[dir], col + dc[dir]

    # 벽에 닿거나 자기 몸에 닿은 경우
    if 0 > nrow or nrow >= N or 0 > ncol or ncol >= N or board[nrow][ncol] == 0:
        end = False

    # 만약 이동한 칸에 사과가 있다면
    elif board[nrow][ncol] == 1:
        board[nrow][ncol] = 0
        snake.appendleft((nrow, ncol))
        row, col = nrow, ncol

    # 사과가 없다면
    else:
        board[nrow][ncol] = 0
        snake.appendleft((nrow, ncol))
        tail_row, tail_col = snake.pop()
        board[tail_row][tail_col] = -1
        row, col = nrow, ncol

    time += 1


print(time)