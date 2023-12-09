'''
바라보는 방향이 존재 : 북(0) 동(1) 남(2) 서(3)

작동을 멈추는 경우 : 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    -> 후진을 할 수 없는 경우

청소가 가능한 경우를 찾기
1. 반시계 방향으로 90도 회전
바라보는 방향 기준 앞 칸이 청소되지 않은 칸인 경우 한 칸 전진.

반시계 방향으로 돌리기
(방향 - 1) % 4
'''

import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
rr, rc, rd = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
cleaned = 0
can_clean = True

while True:
    # 아직 청소되지 않은 경우 청소하기
    if not room[rr][rc]:
        room[rr][rc] = -1
        cleaned += 1

    for d in range(1, 4 + 1):
        nr, nc = rr + dr[(rd - d) % 4], rc + dc[(rd - d) % 4]
        if 0 <= nr < n and 0 <= nc < m and not room[nr][nc]:
            rr, rc = nr, nc
            rd = (rd - d) % 4
            break
    else:
        # 후진해서 이동이 가능한지 확인
        br, bc = rr + dr[(rd - 2) % 4], rc + dc[(rd - 2) % 4]
        if not (0 <= br < n and 0 <= bc < m) or room[br][bc] == 1:
            can_clean = False
        else:
            rr, rc = br, bc

    # 종료 조건
    if not can_clean:
        break

print(cleaned)


