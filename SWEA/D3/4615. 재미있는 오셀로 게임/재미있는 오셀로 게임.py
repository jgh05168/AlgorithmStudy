dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def check(row, col, color):
    for d in range(len(dr)):
        k = 1
        store = []
        while True:
            nrow = row + dr[d] * k
            ncol = col + dc[d] * k
            # 조건 1 : 배열의 인덱스를 벗어나거나, 바꾸려는 자리가 '0'인 경우 == 오슬로 완성이 안되는 경우
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N or board[nrow][ncol] == '0':
                while store:        # 이전 위치에 저장된 값이 있는 경우, 다시 원래대로 돌려놓기
                    brow, bcol, bcolor = store.pop()
                    board[brow][bcol] = bcolor
                break

            # 만약 내 돌을 만난 경우 반복문 종료
            if board[nrow][ncol] == color:
                break
            # 상대 돌을 만난 경우, 혹시모르는 상황에 대비해 위치와 그 위치의 돌 정보 저장
            else:
                store.append([nrow, ncol, board[nrow][ncol]])
                board[nrow][ncol] = color       # 현재 색으로 바꿔줌
            k += 1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 초기 board 세팅
    board = [['0'] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1], board[N // 2][N // 2] = 'W', 'W'
    board[N // 2 - 1][N // 2], board[N // 2][N // 2 - 1] = 'B', 'B'

    for _ in range(M):
        row, col, color = map(int, input().split())
        row -= 1
        col -= 1
        if color == 1:
            board[row][col] = 'B'
            check(row, col, 'B')
        else:
            board[row][col] = 'W'
            check(row, col, 'W')

    w_cnt = 0
    b_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'W':
                w_cnt += 1
            elif board[i][j] == 'B':
                b_cnt += 1

    print(f'#{tc} {b_cnt} {w_cnt}')