'''
n x n
한개의 cell 에는 1개의 core 혹은 전선이 올 수 있음
- 전선은 직선으로만 설치 가능
- 교차해서는 안된다
- 가장자리에 위치한 코어는 이미 전원이 연결된 것으로 간주한다
- 최대한 많은 코어에 전선을 연결했을 경우, 전선 길이의 합을 구하고자 함

최대 12 x 12
코어 개수 12개 이하
전원이 연결되지 않은 코어 존재 가능

풀이:
이미 지나간 코어를 행 x 열 따로 저장하는 방법은 ?
set.update(), set.remove
1. 프로세스 위치들 저장
2. 뽑아서 사용 - 12! x 5
- 전원이 연결되는 경우가 아니라면 의미없음
- 전원이 연결되는 경우에 대해 가지치기 진행
    - 최대 경우보다 작다면 return
'''

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def recur(core_num, val, connected):
    global min_v
    global max_connected
    # 가지치기
    if connected + (len(cores) - core_num) < max_connected:
        return
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

            for brow, bcol in lines:
                cells[brow][bcol] = 0

        recur(core_num + 1, val, connected)


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