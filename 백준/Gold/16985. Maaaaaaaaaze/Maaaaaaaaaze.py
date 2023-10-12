'''
3차원 미로를 탈출할 수 있는 가장 최단 거리를 구하자.

- 모든 경우에 대한 판을 돌려보자.
- 뽑은 면에 대해서 회전 진행
    -> 총 5!번 진행
- 6방면에 대한 bfs 진행
    입구 : (0, 0, 0)
    출구 : (4, 4, 4)
들어갈 때마다 visited 배열 생성
만약 이동한 위치가 최솟값보다 커질 경우 가지치기

'''

from collections import deque
import sys, copy
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dv = [1, -1]


def rotate(floor):
    global temp_list
    for row in range(5):
        for col in range(5):
            temp_list[col][5 - row - 1] = maze[floor][row][col]

    maze[floor] = copy.deepcopy(temp_list)


def bfs(temp_maze, sfloor, srow, scol, exitt):
    global ans
    queue = deque()
    queue.append((sfloor, srow, scol))
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]       # [층][행][열]
    visited[sfloor][srow][scol] = 1

    while queue:
        floor, row, col = queue.popleft()

        if visited[floor][row][col] >= ans:        # 현재 최소값보다 크다면,
            continue

        # 행열 먼저 이동
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < 5 and 0 <= ncol < 5 and not visited[floor][nrow][ncol] and temp_maze[floor][nrow][ncol]:
                if (floor, nrow, ncol) == exitt:        # 도착지점에 온 경우
                    ans = visited[floor][row][col]
                    return
                visited[floor][nrow][ncol] = visited[floor][row][col] + 1
                queue.append((floor, nrow, ncol))
        # 층 이동
        for f in range(len(dv)):
            nfloor = floor + dv[f]
            if 0 <= nfloor < 5 and not visited[nfloor][row][col] and temp_maze[nfloor][row][col]:
                if (nfloor, row, col) == exitt:  # 도착지점에 온 경우
                    ans = visited[floor][row][col]
                    if ans == 12:
                        print(ans)
                        exit()
                    return
                visited[nfloor][row][col] = visited[floor][row][col] + 1
                queue.append((nfloor, row, col))

    return


def per(i):
    if i == 5:
        for enter, exitt in enter_exit:
            sfloor, srow, scol = enter
            efloor, erow, ecol = exitt
            if temp_maze[sfloor][srow][scol] and temp_maze[efloor][erow][ecol]:  # 입구와 출구가 존재하는 경우만 bfs 진행
                # bfs 돌려보기
                bfs(temp_maze, sfloor, srow, scol, exitt)
        return

    for j in range(5):
        if not selected[j]:
            selected[j] = 1
            temp_maze[i] = copy.deepcopy(maze[j])      # 배열 복사
            per(i + 1)

            selected[j] = 0


def select_floor(floor):
    global temp_list
    if floor < 0:
        return

    # rotate 해보기
    for rotate_cnt in range(4):  # 5번 째 돌아가는 경우 원상복구
        rotate(floor)

        select_floor(floor - 1)     # 한바퀴 돌리고 재귀

        # 판들을 모두 돌렸으면 순열로 층을 쌓아보기
        per(0)


# init
maze = []
for _ in range(5):
    part_maze = [list(map(int, input().split())) for _ in range(5)]
    maze.append(part_maze)

ans = int(1e9)

temp_list = [[0] * 5 for _ in range(5)]  # 회전한 층 복사를 위한 배열
enter_exit = [((0, 0, 0), (4, 4, 4)), ((0, 0, 4), (4, 4, 0)), ((0, 4, 0), (4, 0, 4)), ((0, 4, 4), (4, 0, 0))]
selected = [0] * 5
temp_maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]

# 순열로 한 층씩 모두 해보기 - 완탐
select_floor(4)

if ans == int(1e9):
    print(-1)
else:
    print(ans)