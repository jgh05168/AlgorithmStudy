'''
- 궁수의 위치가 한 번 정해지면 다시 이동할 수 없다.

= bfs를 사용해서 거리 내 잡을 수 있는 적들의 최댓값을 구해야 한다.
    - 궁수 위치를 순열로 찾기 : 최악의 경우 15C3 = 455

'''
import sys, copy
from collections import deque
input = sys.stdin.readline

dr = [0, -1, 0]
dc = [-1, 0, 1]


def init():
    tmp = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                tmp += 1
    return tmp


def move_map(enemies, war_map):
    war_map.appendleft([0] * m)
    archers = war_map.pop()
    for col in range(m):
        if war_map[-1][col]:
            enemies -= 1
            war_map[-1][col] = 0
    war_map.pop()
    war_map.append(archers)

    return war_map, enemies


def bfs(archer_loc_list):
    global enemies
    killed = 0
    tmp_enemies = enemies
    queue = deque()
    war_map = copy.deepcopy(grid)

    while tmp_enemies:
        # 항상 초기화
        did_archers = [0] * 3
        attacked = set()
        visited = [[[-1] * m for _ in range(n + 1)] for _ in range(3)]
        for idx, archer_loc in enumerate(archer_loc_list):
            queue.append((n, archer_loc, idx))
            visited[idx][n][archer_loc] = 0

        while queue:
            row, col, archer_num = queue.popleft()

            if visited[archer_num][row][col] >= D:       # 거리 만큼 탐색했으면 종료
                continue

            if did_archers[archer_num]:     # 이미 적을 죽인 궁수면 종료
                continue

            for d in range(len(dr)):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 <= nrow < n and 0 <= ncol < m and visited[archer_num][nrow][ncol] == -1:
                    # 적일 경우 처리
                    if war_map[nrow][ncol]:
                        if (nrow, ncol) not in attacked:
                            killed += 1
                            tmp_enemies -= 1
                            attacked.add((nrow, ncol))
                        did_archers[archer_num] = 1
                        break
                    visited[archer_num][nrow][ncol] = visited[archer_num][row][col] + 1
                    queue.append((nrow, ncol, archer_num))

        for arow, acol in attacked:
            war_map[arow][acol] = 0
        war_map, tmp_enemies = move_map(tmp_enemies, war_map)

    return killed


def dfs(before_idx, fixed_archers, archer_loc_list):
    global max_killed
    if fixed_archers >= 3:

        killed = bfs(archer_loc_list)
        max_killed = max(max_killed, killed)
        return

    for archer_loc in range(before_idx + 1, m):
        if not grid[n][archer_loc]:
            grid[n][archer_loc] = 2
            dfs(archer_loc, fixed_archers + 1, archer_loc_list + [archer_loc])
            grid[n][archer_loc] = 0


n, m, D = map(int, input().split())
grid = deque([list(map(int, input().split())) for _ in range(n)])
grid.append([0] * m)
enemies = init()
max_killed = 0

dfs(-1, 0, [])

print(max_killed)