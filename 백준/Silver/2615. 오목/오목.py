#     6 | 12    5 | 11   3 | 9  1 | 7
dr = [[1, -1], [1, -1], [0, 0], [-1, 1]]
dc = [[0, 0], [1, -1], [1, -1], [1, -1]]

def omoc(row, col, color):
    for d in range(len(dr)):
        uprow, upcol = row, col
        downrow, downcol = row, col
        check = 0
        cur_loc = []
        # down
        while 0 <= downrow < N and 0 <= downcol < N and board[downrow][downcol] == color:
            check += 1
            cur_loc.append((downrow, downcol))
            downrow = downrow + dr[d][0]
            downcol = downcol + dc[d][0]

        # reverse
        while 0 <= uprow < N and 0 <= upcol < N and board[uprow][upcol] == color:
            check += 1
            cur_loc.append((uprow, upcol))
            uprow = uprow + dr[d][1]
            upcol = upcol + dc[d][1]

        check -= 1
        if check == 5:
            cur_loc.sort(key=lambda x : x[1])
            # print(cur_loc)
            return check, cur_loc[0][0], cur_loc[0][1]

    return check, row, col


N = 19
board = [list(map(int, input().split())) for _ in range(N)]
find = False

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 or board[i][j] == 2:
            color = board[i][j]
            check, r, c = omoc(i, j, color)
            if check == 5:
                find = True
                break

    if find == True:
        break

if find == True:
    print(color)
    print(r + 1, c + 1)
else:
    print(0)