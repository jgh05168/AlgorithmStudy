'''

1. 해적 먼저 이동 -> 해적은 가만히 있거나 움직일 수 있다.
    - 벽이랑 막힐 때까지 업데이트
    - 이미 볼 수 있는 부분이라면 그만가도 된다.
2. 수아 이동 -> 만약 해적이랑 마주친다면 움직일 수 없음.
    - 수아가 이미 있다면 상관없다.

종료 조건 : 업데이트 해 줄 queue가 존재하지 않는 경우.
---------------------시간초과------------------------

1. 해적 먼저 bfs 돌려준다.
2. 해적의 시야를 체크
    - 돌린 bfs에 대한 최솟값으로 업데이트
    - row 두 번, col 두 번 적용해줘야지 전체 이동에 대한 최소 시야가 체크된다.
3. 수아 bfs 돌려주기
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def init(suaa, piratee, treasuree):
    find_y, find_v, find_t = False, False, False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'Y':
                suaa.append((i, j))
                visited_sua[i][j] = 0
                find_y = True
            elif grid[i][j] == 'V':
                piratee.append((i, j))
                visited_pirate[i][j] = 0
                find_v = True
            elif grid[i][j] == 'T':
                treasuree = (i, j)
                find_t = True
            if find_v and find_t and find_y:
                return suaa, piratee, treasuree


def pirate_bfs(queue):
    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and visited_pirate[nrow][ncol] == INF and grid[nrow][ncol] != 'I':
                visited_pirate[nrow][ncol] = visited_pirate[row][col] + 1
                queue.append((nrow, ncol))


def update_sight():
    # row : (0, 0)에서 시작
    for row in range(n):
        min_sight = INF
        for col in range(m):
            if grid[row][col] == 'I':
                min_sight = INF
                pirate_move[row][col] = -1
            else:
                if visited_pirate[row][col] < min_sight:
                    min_sight = visited_pirate[row][col]
                pirate_move[row][col] = min(pirate_move[row][col], min_sight)

    # row : (0, m - 1)에서 시작
    for row in range(n):
        min_sight = INF
        for col in range(m - 1, -1, -1):
            if grid[row][col] == 'I':
                min_sight = INF
                pirate_move[row][col] = -1
            else:
                if visited_pirate[row][col] < min_sight:
                    min_sight = visited_pirate[row][col]
                pirate_move[row][col] = min(pirate_move[row][col], min_sight)

    # col : (0, 0)에서 시작
    for col in range(m):
        min_sight = INF
        for row in range(n):
            if grid[row][col] == 'I':
                min_sight = INF
                pirate_move[row][col] = -1
            else:
                if visited_pirate[row][col] < min_sight:
                    min_sight = visited_pirate[row][col]
                pirate_move[row][col] = min(pirate_move[row][col], min_sight)

    # col : (n - 1, 0)에서 시작
    for col in range(m):
        min_sight = INF
        for row in range(n - 1, -1, -1):
            if grid[row][col] == 'I':
                min_sight = INF
                pirate_move[row][col] = -1
            else:
                if visited_pirate[row][col] < min_sight:
                    min_sight = visited_pirate[row][col]
                pirate_move[row][col] = min(pirate_move[row][col], min_sight)


def sua_bfs(queue):
    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and visited_sua[nrow][ncol] == -1 and grid[nrow][ncol] != 'I':
                if visited_sua[row][col] + 1 >= pirate_move[nrow][ncol]:
                    continue
                if (nrow, ncol) == treasure:
                    return True
                visited_sua[nrow][ncol] = visited_sua[row][col] + 1
                queue.append((nrow, ncol))
    return False


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
INF = int(1e9)
pirate_move = [[INF] * m for _ in range(n)]
visited_pirate = [[INF] * m for _ in range(n)]
visited_sua = [[-1] * m for _ in range(n)]
find_treasure = False
sua, pirate, treasure = init(deque(), deque(), tuple())

# 해적 먼저 이동
pirate_bfs(pirate)

# 해적의 시야 업데이트
update_sight()

# 수아 이동
find_treasure = sua_bfs(sua)

if find_treasure:
    print('YES')
else:
    print('NO')