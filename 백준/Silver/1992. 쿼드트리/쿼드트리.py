import sys
input = sys.stdin.readline

def rec(rows, cols):
    rmid = (rows[0] + rows[1]) // 2
    cmid = (cols[0] + cols[1]) // 2

    stack.append('(')
    # 1사분면
    isrec = False
    startval = grid[rows[0]][cols[0]]
    for row in range(rows[0], rmid + 1):
        for col in range(cols[0], cmid + 1):
            if grid[row][col] != startval:  # 만약 값이 같지 않다면 재귀반복
                rec((rows[0], rmid), (cols[0], cmid))
                isrec = True
                break
        if isrec:
            break
    if not isrec:
        stack.append(str(startval))

    # 2사분면
    isrec = False
    startval = grid[rows[0]][cmid + 1]
    for row in range(rows[0], rmid + 1):
        for col in range(cmid + 1, cols[1] + 1):
            if grid[row][col] != startval:  # 만약 값이 같지 않다면 재귀반복
                rec((rows[0], rmid), (cmid + 1, cols[1]))
                isrec = True
                break
        if isrec:
            break
    if not isrec:
        stack.append(str(startval))

    # 3사분면
    isrec = False
    startval = grid[rmid + 1][cols[0]]
    for row in range(rmid + 1, rows[1] + 1):
        for col in range(cols[0], cmid + 1):
            if grid[row][col] != startval:  # 만약 값이 같지 않다면 재귀반복
                rec((rmid + 1, rows[1]), (cols[0], cmid))
                isrec = True
                break
        if isrec:
            break
    if not isrec:
        stack.append(str(startval))

    # 4사분면
    isrec = False
    startval = grid[rmid + 1][cmid + 1]
    for row in range(rmid + 1, rows[1] + 1):
        for col in range(cmid + 1, cols[1] + 1):
            if grid[row][col] != startval:  # 만약 값이 같지 않다면 재귀반복
                rec((rmid + 1, rows[1]), (cmid + 1, cols[1]))
                isrec = True
                break
        if isrec:
            break
    if not isrec:
        stack.append(str(startval))

    stack.append(')')


N = int(input().rstrip())

grid = [list(map(int, input().rstrip())) for _ in range(N)]
startval = grid[0][0]
if N == 1:
    print(f"{startval}")

else:
    check_all = True
    for row in range(N):
        for col in range(N):
            if grid[row][col] != startval:
                srows, scols = (0, N - 1), (0, N - 1)
                stack = []
                rec(srows, scols)
                check_all = False
                print(''.join(stack))
                break
        if not check_all:
            break
    else:
        print(f"{startval}")
