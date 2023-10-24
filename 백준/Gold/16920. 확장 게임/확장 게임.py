'''
새로 생긴 애들에 대해서만 bfs 돌려주기
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def expand(castle, castle_land):
    global empty
    expand_list = []
    queue = castle_land
    for srow, scol in castle_land:
        visited[srow][scol] = 0

    while queue:
        row, col = queue.popleft()
        if visited[row][col] + 1 > S[castle]:
            continue
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] == -1 and grid[nrow][ncol] == '.':

                visited[nrow][ncol] = visited[row][col] + 1
                queue.append((nrow, ncol))
                expand_list.append((nrow, ncol))
                grid[nrow][ncol] = str(castle)
                empty -= 1
                castle_count[castle] += 1

    if expand_list == []:
        return False, deque(expand_list)
    else:
        return True, deque(expand_list)


N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
grid = [list(input().rstrip()) for _ in range(N)]
castle_list = [deque() for _ in range(P + 1)]       # 각각의 성 좌표를 리스트가 아닌 deque()로 초기화
castle_count = {}
empty = 0
visited = [[-1] * M for _ in range(N)]
# 딕셔너리 초기화
for i in range(P + 1):
    castle_count.update({i: 0})
# 각자 땅들 찾기
for i in range(N):
    for j in range(M):
        if grid[i][j] == '#':
            continue
        elif grid[i][j] == '.':
            empty += 1
        else:
            castle_list[int(grid[i][j])].append((i, j))
            castle_count[int(grid[i][j])] += 1

case = 0
valid_list = [True] * (P + 1)
castle = 1
while empty:
    if case == P:
        break
    if not castle:
        castle = (castle + 1) % (P + 1)
        continue

    if valid_list[castle]:
        check_valid, castle_list[castle] = expand(castle, castle_list[castle])
        if not check_valid:
            case += 1
            valid_list[castle] = False
    castle = (castle + 1) % (P + 1)

for castle in range(1, P + 1):
    print(castle_count[castle], end=' ')

