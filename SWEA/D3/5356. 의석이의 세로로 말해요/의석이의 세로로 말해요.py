T = int(input())

for tc in range(1, T + 1):
    N = 5
    board = [list(input()) for _ in range(N)]
    M = 0
    for i in range(N):
        if M < len(board[i]):
            M = len(board[i])

    string = ''
    for col in range(M):
        for row in range(N):
            try:
                string += board[row][col]
            except:
                string += ''

    print(f'#{tc} {string}')