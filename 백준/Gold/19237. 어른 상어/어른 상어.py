'''
상어만 남아있음

1이상 M이하 자연수가 붙어있고, 번호는 모두 다르다.
- 1의 번호를 가진 상어가 가장 강력하다

1. 맨 처음 모든 상어가 자신의 위치에 냄새를 뿌린다.
2. 1초마다 모든 상어가 상하좌우로 인접한 칸 중 하나로 이동 후 그 칸에 냄새를 뿌린다.
    - 냄새는 상어가 k번 이동하면 사라짐
    - 방향을 잡을 때는
        1. 아무 냄새가 없는 칸으로 방향을 잡음
        2. 그런 칸이 없으면 자신의 냄새가 있는 칸으로 방향을 잡음
        - 이동 우선순위 : 상어마다 다름
    - 맨처음 방향은 입력. 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.
3. 상어가 같은 위치에 도착했을 경우, 상어숫자가 낮은 상어가 살아남고, 높은 상어는 퇴출된다.
    - 냄새는 그대로 남음
- 각 상어는 현재 방향에 따른 우선순위를 갖고 있다.

현재 상어의 번호, 위치, 방향 정보를 가져야한다.
냄새를 뿌린 위치는 따로 배열에 저장한 뒤 전체 과정이 종료되고 -1을 진행한다.

출력 : 1번 상어만 격자에 남게 되긲지 몇 초가 걸리는지 출력
1000초가 넘어도 다른 상어가 남아있다면 -1 출력
'''

from collections import defaultdict
import sys
input = sys.stdin.readline

#    위  아  왼  오
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def set_smell(sharks):
    # 1. 모든 상어가 자신의 위치에 냄새를 뿌린다.
    for shark in range(sharks):
        srow, scol = sharks_info[shark][0], sharks_info[shark][1]
        smell[srow][scol] = (shark, k)
        smell_loc.add((srow, scol))


def shark_move():
    global sharks
    shark_from_to = [0 for _ in range(m)]

    for shark in range(m):
        # 이미 죽은 상어라면, continue
        if not sharks_info[shark]:
            continue

        row, col, sd = sharks_info[shark]

        # 먼저 빈 칸이 있는지 체크
        for d in shark_dir[shark][sd]:
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < n and not smell[nrow][ncol]:
                sharks_info[shark] = (nrow, ncol, d)
                shark_from_to[shark] = (row, col, nrow, ncol)
                break
        # 빈 칸이 없다면 자신의 냄새가 있는 칸으로 이동
        else:
            for d in shark_dir[shark][sd]:
                nnrow, nncol = row + dr[d], col + dc[d]
                if 0 <= nnrow < n and 0 <= nncol < n:
                    if smell[nnrow][nncol][0] == shark:
                        sharks_info[shark] = (nnrow, nncol, d)
                        shark_from_to[shark] = (row, col, nnrow, nncol)
                        break

    # 마지막에 상어 위치 업데이트
    for shark in range(m):
        if not shark_from_to[shark]:
            continue
        br, bc, nr, nc = shark_from_to[shark]
        if grid[nr][nc] >= 0:    # 잡아먹힌 경우. 냄새는 남는다
            sharks -= 1
            grid[br][bc] = -1
            sharks_info[shark] = 0
        else:
            smell[nr][nc] = (shark, k)
            smell_loc.add((nr, nc))
            grid[nr][nc] = grid[br][bc]
            grid[br][bc] = -1




n, m, k = map(int, input().split())     # n : 격자 크기, m : 상어 마리 수 k : 냄새 사라지는 횟수
grid = [list(map(int, input().split())) for _ in range(n)]
smell = [[0] * n for _ in range(n)]
smell_loc = set()
sharks_info = [[0] for _ in range(m)]

dir_init = list(map(int, input().split()))
# 상어 업데이트
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            grid[i][j] -= 1
            sharks_info[grid[i][j]] = (i, j, dir_init[grid[i][j]] - 1)
        else:
            grid[i][j] = -1

shark_dir = [defaultdict(list) for _ in range(m)]
for shark in range(m):
    for i in range(4):
        st, nd, rd, th = map(int, input().split())
        shark_dir[shark][i] = [st -1, nd - 1, rd - 1, th - 1]


set_smell(m)
time = 0
sharks = m
while time <= 1000:
    # 2-0. 냄새를 하나 줄이고 시작하자
    new_smell_loc = set()
    while smell_loc:
        sr, sc = smell_loc.pop()
        if not smell[sr][sc][1]:
            smell[sr][sc] = 0
            continue
        shark_num, s_time = smell[sr][sc]
        smell[sr][sc] = (shark_num, s_time - 1)
        new_smell_loc.add((sr, sc))
    smell_loc = new_smell_loc
    # 2. 1초마다 모든 상어가 상하좌우로 인접한 칸 중 하나로 이동 후 그 칸에 냄새를 뿌린다.
    shark_move()

    time += 1
    if sharks == 1:
        break

if time > 1000:
    print(-1)
else:
    print(time)
