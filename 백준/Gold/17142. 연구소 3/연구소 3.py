'''
바이러스를 둘 수 있는 위치를 배열에 저장해둔 뒤 순열로 뽑아가며 bfs 진행

모든 빈칸에 바이러스를 퍼뜨려야 한다. -> 빈칸존재 x
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(viruses):
    global min_spread
    empty_spaces = spaces
    queue = deque(viruses)
    visited = [[-1] * N for _ in range(N)]
    for srow, scol, vcnt in queue:
        visited[srow][scol] = 0

    while queue:
        row, col, v_cnt = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and visited[nrow][ncol] == -1 and lab[nrow][ncol] != 1:
                if lab[nrow][ncol] != 2:
                    queue.append((nrow, ncol, 0))
                    empty_spaces -= 1
                    if lab[row][col] == 2 and (row, col) not in viruses:
                        visited[nrow][ncol] = visited[row][col] + v_cnt + 1
                    else:
                        visited[nrow][ncol] = visited[row][col] + 1
                else:
                    queue.append((nrow, ncol, v_cnt + 1))
                    visited[nrow][ncol] = visited[row][col]


    if not empty_spaces:
        min_spread = min(min_spread, max(map(max, visited)))


def permutation(start, virus_cnt, viruses):
    if virus_cnt == M:
        bfs(viruses)
        return

    for per in range(start, vn):
        if not selected[per]:
            selected[per] = 1
            permutation(per + 1, virus_cnt + 1, viruses + [virus_locs[per]])
            selected[per] = 0


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus_locs = []
spaces = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_locs.append((i, j, 0))
        elif lab[i][j] == 1:
            continue
        else:
            spaces += 1

vn = len(virus_locs)
selected = [0] * vn
min_spread = int(1e9)

permutation(0, 0, [])

if min_spread == int(1e9):
    print(-1)
else:
    print(min_spread)