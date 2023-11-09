'''
통나무 가운데를 기준으로 가능한 경우를 판단

각 방향 3가지 경우 확인. 이후 갈 수 있으면 queue에 삽입
통나무가 수직인지 수평인지 확인해주는 변수도 같이 보내주기
visited는 가운데 부분만 기록하기
'''

from collections import deque
import sys
input = sys.stdin.readline

# 상 하 좌 우
dr = [[(-1, -1, -1), (1, 1, 1), (0, 0, 0), (0, 0, 0)], [(-2, -1, 0), (0, 1, 2), (-1, 0, 1), (-1, 0, 1)]]
dc = [[(-1, 0, 1), (-1, 0, 1), (-2, -1, 0), (0, 1, 2)], [(0, 0, 0), (0, 0, 0), (-1, -1, -1), (1, 1, 1)]]

round_dr = [0, 1, 1, 1, 0, -1, -1, -1]
round_dc = [1, 1, 0, -1, -1, -1, 0, 1]

def init():
    # 시작 통나무, 도착 지점 찾기
    start_log, end_log = 0, 0
    slog, elog = [0, 0], [0, 0]
    find_s, find_e = False, False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'E':
                end_log += 1
                if end_log == 2:
                    find_e = True
                    elog = [i, j]
            if grid[i][j] == 'B':
                start_log += 1
                if start_log == 2:
                    find_s = True
                    slog = [i, j]

            if find_e and find_s:
                break
        if find_e and find_s:
            break

    # 통나무 방향 찾기
    direction = 0       # 가로 : 0 / 세로 : 1
    for d in (-1, 1):
        ncol = slog[1] + d
        if 0 <= ncol < n and grid[slog[0]][ncol] == 'B':
            direction = 0
        else:
            direction = 1
    slog.append(direction)
    direction = 0       # 가로 : 0 / 세로 : 1
    for d in (-1, 1):
        ncol = elog[1] + d
        if 0 <= ncol < n and grid[elog[0]][ncol] == 'E':
            direction = 0
        else:
            direction = 1
    elog.append(direction)

    return slog, elog


def validGo(nrow, ncol, direction, d):
    # 세가지 방향 모두 갈 수 있다면 이동가능
    for dd in range(len(dr[direction][d])):
        crow, ccol = nrow + dr[direction][d][dd], ncol + dc[direction][d][dd]
        if not (0 <= crow < n and 0 <= ccol < n and grid[crow][ccol] != '1'):
            return False
    return True


def bfs(srow, scol, sdirection):
    queue = deque()
    queue.append((srow, scol, sdirection))
    visited[sdirection][srow][scol] = 0

    while queue:
        row, col, direction = queue.popleft()

        # 상하좌우 이동부터
        for d in range(len(dr[direction])):
            check_go = False
            nrow, ncol = row + dr[direction][d][1], col + dc[direction][d][1]
            if 0 <= nrow < n and 0 <= ncol < n and visited[direction][nrow][ncol] == -1:
                check_go = validGo(row, col, direction, d)
            if check_go:
                if [nrow, ncol, direction] == elog:
                    return visited[direction][row][col] + 1
                visited[direction][nrow][ncol] = visited[direction][row][col] + 1
                queue.append((nrow, ncol, direction))

        # 통나무 돌리기
        if visited[(direction + 1) % 2][row][col] == -1:
            for d in range(len(round_dr)):
                nrow, ncol = row + round_dr[d], col + round_dc[d]
                if not (0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] != '1'):
                    break
            else:
                if [row, col, (direction + 1) % 2] == elog:
                    return visited[direction][row][col] + 1
                visited[(direction + 1) % 2][row][col] = visited[direction][row][col] + 1
                queue.append((row, col, (direction + 1) % 2))

    return 0



n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
visited = [[[-1] * n for _ in range(n)] for _ in range(2)]
slog, elog = init()

print(bfs(slog[0], slog[1], slog[2]))