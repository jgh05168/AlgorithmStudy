'''
구슬탈출 2

빨간 구슬을 구멍을 통해 빼내는 것

중력을 이용해서 이리저리 굴린다 -> 갈 수 있는 공간까지 가본다
파란구슬이 빠지면 실패이다.

1. 4방향 모두 굴려보기
2. 모든 경우에 대해서 판단해보기 -> 잘라내기

10번 이하로 움직인다는 조건이 주어진다. -> 백트래킹

- 빨간공, 파란공 에 대한 정보를 각각 다음 재귀함수로 넘겨준다.
    - 구멍에 도달하면 boolean 전달
    - 아이라면 벽 or 상대 공에 닿을 때까지 직진
- 옮기기 전 위치를 저장하는 배열이 존재해야 한다. -> stack으로 짜도 무방

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

#    동  남  서  북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def red_move(d, red):
    row, col = red[0], red[1]
    board[red[0]][red[1]] = '.'
    goal = False

    while 1 <= row + dr[d] < N - 1 and 1 <= col + dc[d] < M - 1 and board[row + dr[d]][col + dc[d]] == '.':
        row, col = row + dr[d], col + dc[d]
    # 골인지점인지 판단
    if board[row + dr[d]][col + dc[d]] == 'O':
        row, col = row + dr[d], col + dc[d]
        goal = True
        return (row, col), goal

    board[row][col] = 'R'
    return (row, col), goal


def blue_move(d, blue):
    row, col = blue[0], blue[1]
    board[blue[0]][blue[1]] = '.'
    goal = False

    while 1 <= row + dr[d] < N - 1 and 1 <= col + dc[d] < M - 1 and board[row + dr[d]][col + dc[d]] == '.':
        row, col = row + dr[d], col + dc[d]
    # 골인지점인지 판단
    if board[row + dr[d]][col + dc[d]] == 'O':
        row, col = row + dr[d], col + dc[d]
        goal = True
        return (row, col), goal

    board[row][col] = 'B'
    return (row, col), goal


def dfs(move, red, blue, direction, redcheck, bluecheck):
    global min_move
    # 종료 조건
    if redcheck and not bluecheck:      # 빨간공만을 무사히 넣은 경우
        min_move = min(min_move, move)
        return

    # 현재 횟수보다 최소 횟수가 크거나, 횟수가 10번을 넘거나, 파란공이 들어간 경우 종료
    if min_move < move or move > 10 or bluecheck:
        return

    for d in range(len(dr)):
        if d == direction:
            continue
        # 4 방향 모두 누가 먼저 움직이는지 다르므로 판단해주어야 한다.
        # 좌 우
        if d == 0:          # 우
            if red[1] < blue[1]:    # 파란공이 더 오른쪽에 있다면
                nblue, nblue_check = blue_move(d, blue)
                nred, nred_check = red_move(d, red)
            else:
                nred, nred_check = red_move(d, red)
                nblue, nblue_check = blue_move(d, blue)
        elif d == 1:          # 하
            if red[0] < blue[0]:    # 파란공이 빨간공보다 더 아래에 있다면
                nblue, nblue_check = blue_move(d, blue)
                nred, nred_check = red_move(d, red)
            else:
                nred, nred_check = red_move(d, red)
                nblue, nblue_check = blue_move(d, blue)
        elif d == 2:        # 좌
            if red[1] > blue[1]:     # 파란공이 더 왼쪽에 있다면
                nblue, nblue_check = blue_move(d, blue)
                nred, nred_check = red_move(d, red)
            else:
                nred, nred_check = red_move(d, red)
                nblue, nblue_check = blue_move(d, blue)
        else:           # 상
            if red[0] > blue[0]:     # 파란공이 빨간 공보다 위에 있다면
                nblue, nblue_check = blue_move(d, blue)
                nred, nred_check = red_move(d, red)
            else:
                nred, nred_check = red_move(d, red)
                nblue, nblue_check = blue_move(d, blue)

        # 만약 빨간공 파란공 위치가 이전과 같다면
        if red == nred and blue == nblue:
            continue

        # 다음 단계로 보내기
        dfs(move + 1, nred, nblue, d, nred_check, nblue_check)

        # 이전 위치로 되돌리기
        if red != nred:
            board[red[0]][red[1]] = 'R'
            if not nred_check:
                board[nred[0]][nred[1]] = '.'

        if blue != nblue:
            board[blue[0]][blue[1]] = 'B'
            if not nblue_check:
                board[nblue[0]][nblue[1]] = '.'



N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

# 초기 빨간 공, 파란 공, 구멍 위치 찾기
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            hole = (i, j)

# 게임 시작
min_move = 11
dfs(0, red, blue, -1, False, False)

if min_move == 11:
    print(-1)
else:
    print(min_move)