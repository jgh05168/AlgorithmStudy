'''
1. 자리 하나에는 cell 혹은 전선만 가능
2. 가장자리는 건들면  안돼 - 전원연결
3. 전선은 절대 교차하면 안된다.
4. core와 전원을 연결하는 전선은 직선으로만 설치 가능
5. 가장자리 core는 전원이 연결된 것으로 본다.
'''

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def recur(core_num, val, connected):
    global min_v
    global max_connected
    if core_num > len(cores) - 1:
        if max_connected < connected:
            max_connected = connected
            min_v = val
        elif max_connected == connected:
            if min_v > val:
                min_v = val
        return

    else:
        row, col = cores[core_num]
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            go = True
            temp = 0
            lines = []
            while 0 <= nrow < N and 0 <= ncol < N:
                if cells[nrow][ncol]:
                    go = False
                    break
                lines.append((nrow, ncol))
                cells[nrow][ncol] = 2
                nrow, ncol = nrow + dr[d], ncol + dc[d]
                temp += 1

            if go:
                recur(core_num + 1, val + temp, connected + 1)
            else:
                recur(core_num + 1, val, connected)

            for brow, bcol in lines:
                cells[brow][bcol] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cells = [list(map(int, input().split())) for _ in range(N)]

    cores = []
    # 가장자리 아닌 코어들 좌표 저장
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if cells[i][j]:
                cores.append((i, j))

    min_v = N ** 2
    max_connected = 0
    recur(0, 0, 0)
    print(f'#{tc} {min_v}')
