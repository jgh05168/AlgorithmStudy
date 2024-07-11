'''
공기청정기는 항상 1번 열에 설치되어 있음(두 행 차지)

1. 미세먼지 확산. (모든 칸에서 인접한 네 방향으로 동시에 일어남)
    1-1. 인접한 방향에 공기청정기가 있거나, 칸이 없으면 확산이 일어나지 않음
    1-2. A // 5 만큼 확산
    1-3. 확산 전에 남은 미세먼지 양은 (확산 전 - (확산 후 양 x 방향 개수))
    1-4. 확산될 때 미세먼지가 있다면, 함쳐진다.
2. 공기청정기 작동
    위쪽 공청기는 반시계방향으로 순환
    아래쪽은 시계방향으로 순환
    2-1. 바람 불 때, 미세먼지가 한 칸씩 이동한다.
    2-2. 공청기로 들어간 미세먼지는 모두 정화된다.(0)
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def move_dust(dusts):
    # 새로운 맵 생성
    new_room = [[0] * C for _ in range(R)]
    new_room[top[0]][top[1]], new_room[bottom[0]][bottom[1]] = -1, -1

    while dusts:
        row, col = dusts.popleft()
        dust = room[row][col]
        # 네 방향 체크
        cnt_dusts = 0
        for d in range(len(dr)):
            nr, nc = row + dr[d], col + dc[d]
            if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                new_room[nr][nc] += dust // 5
                cnt_dusts += 1

        # 움직인 양 계산해서 현재 dust 조절
        new_room[row][col] += dust - dust // 5 * cnt_dusts

    return new_room


def machine_action():
    # 새로운 맵 생성
    new_room = [[0] * C for _ in range(R)]
    new_room[top[0]][top[1]], new_room[bottom[0]][bottom[1]] = -1, -1

    # top부터 반시계로 이동
    d = 0
    r, c = top[0], 1
    while True:
        nr, nc = r + dr[d], c + dc[d]
        if (nr, nc) == top:
            break
        if 0 <= nr <= top[0] and 0 <= nc < C:
            new_room[nr][nc] = room[r][c]
            r, c = nr, nc
        else:
            d = (d - 1) % 4

    # bottom도 시계 방향으로 이동
    d = 0
    r, c = bottom[0], 1
    while True:
        nr, nc = r + dr[d], c + dc[d]
        if (nr, nc) == bottom:
            break
        if bottom[0] <= nr < R and 0 <= nc < C:
            new_room[nr][nc] = room[r][c]
            r, c = nr, nc
        else:
            d = (d + 1) % 4

    # 나머지 해당사항 없는 친구들 값 복사해주기
    for i in range(R):
        if i in [0, R - 1, bottom[0], top[0]]:
            continue
        for j in range(1, C - 1):
            new_room[i][j] = room[i][j]

    return new_room

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 공청기 위치 찾기
top, bottom = (-1, -1), (-1, -1)
dusts = deque()
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            if top == (-1, -1):
                top = (i, j)
            else:
                bottom = (i, j)
        elif room[i][j]:
            dusts.append((i, j))

for _ in range(T):
    # 0. 미세먼지 배열 위치 찾기
    dusts = deque()
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                dusts.append((i, j))

    # 1. 미세먼지 이동
    room = move_dust(dusts)

    # 2. 공청기 순환
    room = machine_action()

ans = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            ans += room[i][j]

print(ans)