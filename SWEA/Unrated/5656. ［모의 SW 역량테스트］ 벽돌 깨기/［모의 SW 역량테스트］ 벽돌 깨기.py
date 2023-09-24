'''
N < 4 --> 재귀로 풀어도 된다.

4 * 12 * 15 * 12 * 15 * 9 * 4 < 15 * 20000000

완전탐색 + bfs
하나씩 재귀적으로 완전탐색 + bfs 후 터트릴 수 있는 모든 블럭의 정보를 저장
직접 block의 구조를 건들여기며 터트려도 어차피 재귀이기 때문에 상관없다.
재귀 한 번 돌 때마다 visited를 사용해서 연쇄반응 시 이미 터졌는지 안터졌는지를 판단
시뮬레이션처럼 벽돌을 아래로 내려주는 과정도 필요하다.

정답 : 가장 많이 터질 수 있는 block의 개수를 return

'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def move_blocks():
    move_grid = deque()
    # 아래부터 탐색
    for mrow in range(H - 1, -1, -1):
        for mcol in range(W):
            if board[mrow][mcol]:
                power = board[mrow][mcol]
                if mrow < H - 1:
                    row_update = mrow
                    move = False
                    while row_update + 1 < H and not board[row_update + 1][mcol]:
                        row_update += 1
                        move = True
                    if move:
                        move_grid.append((mrow, mcol, power))
                        board[mrow][mcol] = 0
                        board[row_update][mcol] = power

    return move_grid
def bfs(srow, scol, power):
    queue = deque()
    queue.append((srow, scol, power))
    crash_grid = deque()        # 벽돌을 깨부순 곳 체크(재귀 실패 시 다시 원래 숫자로 되돌려야 한다)
    visited = [[0] * W for _ in range(H)]
    visited[srow][scol] = 1

    crash_grid.append((srow, scol, power))  # 초기 위치 저장
    block_cnt = 1
    board[srow][scol] = 0
    while queue:
        row, col, power = queue.popleft()

        for d in range(len(dr)):
            for p in range(power):
                nrow, ncol = row + dr[d] * p, col + dc[d] * p
                if 0 <= nrow < H and 0 <= ncol < W and not visited[nrow][ncol] and board[nrow][ncol]:
                    queue.append((nrow, ncol, board[nrow][ncol]))
                    visited[nrow][ncol] = 1
                    # 보드의 칸 시뮬 시작
                    crash_grid.append((nrow, ncol, board[nrow][ncol]))
                    board[nrow][ncol] = 0
                    block_cnt += 1

    return block_cnt, crash_grid


def crash(shoot, blocks):
    global max_block
    if shoot == N:
        if max_block < blocks:
            max_block = blocks
        return

    # 다 부쉈다면
    if blocks == total_blocks:
        max_block = blocks
        return

    selected = [0] * W          # 한 줄이 선택되었는지 체크하는 배열
    for col in range(W):
        for row in range(H):
            # 맨 위에 모든 칸을 다 돌았다면 return
            # 벽돌이 존재한다면 bfs 진행
            if board[row][col] and not selected[col]:
                selected[col] = 1
                # 벽돌 깨부수기
                crash_blocks, crashed_list = bfs(row, col, board[row][col])
                # 벽돌 내리기
                move_list = move_blocks()
                crash(shoot + 1, blocks + crash_blocks)
                # 이전 상태로 되돌리기
                # 내려오기 전 위치로 이동
                for mrow, mcol, power in move_list:
                    board[mrow][mcol] = power
                # 터지기 전 위치에 값 저장
                for crow, ccol, power in crashed_list:
                    board[crow][ccol] = power


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    total_blocks = 0
    for i in range(H):
        for j in range(W):
            if board[i][j]:
                total_blocks += 1

    max_block = 0

    crash(0, 0)
    print(f'#{tc} {total_blocks - max_block}')