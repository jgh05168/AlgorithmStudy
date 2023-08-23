dr = [(0, 0), (1, -1), (1, -1), (1, -1)]
dc = [(1, -1), (1, -1), (0, 0), (-1, 1)]

def checkBingo():
    find = 0
    # 가로
    for row in range(N):
        cnt = 0
        for col in range(N):
            if bingo[row][col] == 0:
                cnt += 1
        if cnt == 5:
            find += 1

    # 세로
    for col in range(N):
        cnt = 0
        for row in range(N):
            if bingo[row][col] == 0:
                cnt += 1
        if cnt == 5:
            find += 1

    # 정대각선
    row, col = 0, 0
    cnt = 0
    for i in range(N):
        if bingo[row + i][col + i] == 0:
            cnt += 1
    if cnt == 5:
        find += 1

    # 역대각선
    row, col = 0, N - 1
    cnt = 0
    for i in range(N):
        if bingo[row + i][col - i] == 0:
            cnt += 1
    if cnt == 5:
        find += 1


    if find >= 3:
        return 1
    else:
        return 0


bingo = [list(map(int, input().split())) for _ in range(5)]
N = 5
getnumb = []
for i in range(5):
    get = list(map(int, input().split()))
    getnumb.extend(get)

cnt = 1
while getnumb:
    numb = getnumb.pop(0)
    # print(numb)
    # for i in range(5):
    #     print(*bingo[i])
    # print()
    binggo = False
    for row in range(N):
        for col in range(N):
            if bingo[row][col] == numb:
                bingo[row][col] = 0
                check = checkBingo()
                if check:
                    binggo = True

            if binggo:
                break

        if binggo:
            break
    if check:
        break
    else:
        cnt += 1

if cnt > 25:
    exit()
else:
    print(cnt)
