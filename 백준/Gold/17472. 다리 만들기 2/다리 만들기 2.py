'''
1. 각 섬 번호 매겨주기
2. 1번 섬부터 시작해서 직선으로 뻗어나가기
3. 다른 섬에 도달했다면 다시 bfs를 돌려주어 섬 영역 체크 및 1번 섬으로 영역 바꿔주기
    3-1. 1번 섬 리스트에 바뀐 영역 추가해주기
- 모든 섬을 찾을 때까지 반복

이후 다리의 수 출력

[추가]
크루스칼 알고리즘 사용한 풀이
https://ku-hug.tistory.com/160
'''

from collections import deque, defaultdict
import sys, copy
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
island_dict = defaultdict(int)

def init():
    i_idx = 1
    f_island = deque()
    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] and not v[i][j]:
                queue = deque()
                queue.append((i, j))
                v[i][j] = 1
                island_dict[i_idx] = 0
                if i_idx == 1:
                    f_island.append((i, j, -1))
                else:
                    grid[i][j] = i_idx
                while queue:
                    r, c = queue.popleft()
                    for d in range(len(dr)):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < m and not v[nr][nc] and grid[nr][nc]:
                            grid[nr][nc] = i_idx
                            queue.append((nr, nc))
                            if i_idx == 1:
                                f_island.append((nr, nc, -1))
                            v[nr][nc] = 1
                i_idx += 1

    return f_island, i_idx - 1



def island_check(srow, scol, island_num):
    global get_island
    visited = [[0] * m for _ in range(n)]
    visited[srow][scol] = 1
    queue = deque()
    queue.append((srow, scol))
    grid[srow][scol] = 1
    island_dict[island_num] = 1
    get_island += 1
    first_island.append((srow, scol, -1))

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and grid[nrow][ncol] == island_num:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = 1
                grid[nrow][ncol] = 1
                first_island.append((nrow, ncol, -1))       # 첫번째 섬


def make_bridge(island_init):
    global bridges
    queue = copy.deepcopy(island_init)
    visited = [[[-1] * m for _ in range(n)] for _ in range(4)]
    for srow, scol, sd in queue:
        for ssd in range(4):
            visited[ssd][srow][scol] = 0

    while queue:
        row, col, cur_d = queue.popleft()

        if cur_d == -1:
            for d in range(len(dr)):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 <= nrow < n and 0 <= ncol < m and visited[d][nrow][ncol] == -1 and not grid[nrow][ncol]:
                    queue.append((nrow, ncol, d))
                    visited[d][nrow][ncol] = 1
        else:
            nrow, ncol = row + dr[cur_d], col + dc[cur_d]
            if 0 <= nrow < n and 0 <= ncol < m and visited[cur_d][nrow][ncol] == -1:
                # 섬을 찾은 경우
                if grid[nrow][ncol]:
                    if visited[cur_d][row][col] == 1:      # 다리가 하나만 있는 경우는 continue
                        continue
                    island_check(nrow, ncol, grid[nrow][ncol])
                    bridges += visited[cur_d][row][col]
                    return True
                else:
                    queue.append((nrow, ncol, cur_d))
                    visited[cur_d][nrow][ncol] = visited[cur_d][row][col] + 1

    return False


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

first_island, islands = init()
get_island = 1
bridges = 0
while get_island != islands:
    bridge_valid = make_bridge(first_island)
    if not bridge_valid:
        print(-1)
        exit()

print(bridges)
