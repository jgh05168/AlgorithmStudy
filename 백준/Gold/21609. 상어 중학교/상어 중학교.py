'''
검은블록 : -1
무지개블록 : 0
일반블록 : 나머지

인접 칸 : 상하좌우

블록 그룹 조건
1. 일반 블록이 적어도 하나 있어야한다.
2. 일반 블록의 색은 모두 같아야한다.
3. 검은색 블록은 있으면 안된다.
4. 무지개블록은 상관없다.
5. 모든 블록의 개수는 2보다 크거나 같고, 이동가능해야한다.
6. 블록 그룹의 기준은 무지개블록이 아닌 블록 중 행.열 오름차순

오토 플레이 기능
1. 크기가 가장 큰 블록을 찾는다.
    1-1. 여러개일 경우 무지개 블록의 수가 가장 많은 블록
    1-2. 행. 열 순
2. 1에서 찾은 블록 제거. 블록의 수^2만큼 점수 획들
3. 중력 작용
    3-1. 검은색 블록은 제외.
4. 반시계 방향으로 rotate
5. 다시 중력 작용
'''


from collections import deque
import heapq, sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol, color):
    global max_rainbow_blocks, max_block_cnt, max_block, max_row, max_col
    queue = deque()
    queue.append((srow, scol))
    visited = [[0] * N for _ in range(N)]
    visited[srow][scol] = 1
    color_visited[srow][scol] = 1
    block_cnt = 1
    rainbow_blocks = 0
    temp_block = [(srow, scol)]

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol] and (not blocks[nrow][ncol] or blocks[nrow][ncol] == color):
                if not blocks[nrow][ncol]:
                    rainbow_blocks += 1
                else:
                    color_visited[nrow][ncol] = 1
                visited[nrow][ncol] = 1
                queue.append((nrow, ncol))
                temp_block.append((nrow, ncol))
                block_cnt += 1

    if block_cnt >= 2:
        if max_block_cnt < block_cnt:
            max_block_cnt = block_cnt
            max_rainbow_blocks = rainbow_blocks
            max_row = srow
            max_col = scol
            max_block = temp_block
        elif max_block_cnt == block_cnt:
            if max_rainbow_blocks < rainbow_blocks:
                max_rainbow_blocks = rainbow_blocks
                max_row = srow
                max_col = scol
                max_block = temp_block
            elif max_rainbow_blocks == rainbow_blocks:           # 무지개 블록까지 같다면
                if max_row < srow:
                    max_row = srow
                    max_col = scol
                    max_block = temp_block
                elif max_row == srow:
                    if max_col < scol:
                        max_col = scol
                        max_block = temp_block

        return True

    return False


def gravity():
    # 아래서부터 위로 작용해야한다.
    for grow in range(N - 2, -1, -1):
        for gcol in range(N):
            if blocks[grow][gcol] != -1:        # 검정 블록은 중력 작용 x
                tmp_row, tmp_col = grow, gcol
                while tmp_row + 1 < N:      # 중력은 row에 대해서만 작용
                    if blocks[tmp_row + 1][tmp_col] != -2:      # 내려가고 싶은 칸이 빈칸이 아니라면 종료
                        break
                    blocks[tmp_row + 1][tmp_col] = blocks[tmp_row][tmp_col]
                    blocks[tmp_row][tmp_col] = -2
                    tmp_row += 1


def rotate():
    global blocks
    temp_blocks = [[0] * N for _ in range(N)]
    for rrow in range(N):
        for rcol in range(N):
            temp_blocks[N - rcol - 1][rrow] = blocks[rrow][rcol]

    blocks = temp_blocks


N, M = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]
point = 0

while True:
    max_block_cnt, max_rainbow_blocks, max_row, max_col = 0, 0, 0, 0
    max_block = []
    final_find = False
    # 블록 그룹 먼저 찾기 - 가장 큰 블록 그룹도 찾아준다.
    color_visited = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if blocks[row][col] > 0 and not color_visited[row][col]:
                find = bfs(row, col, blocks[row][col])
                if find:
                    final_find = True

    # 무한반복 종료조건 : 더이상 옮길 블록조합이 없다면
    if not final_find:
        break

    # 가장 큰 블록 그룹을 없애주기
    # 빈 칸 : -2로 설정
    point += (max_block_cnt ** 2)       # 점수매기기
    for mrow, mcol in max_block:
        blocks[mrow][mcol] = -2

    # 중력 작용
    gravity()

    # 90도 반시계방향으로 회전
    rotate()

    # 다시 중력 작용
    gravity()

print(point)