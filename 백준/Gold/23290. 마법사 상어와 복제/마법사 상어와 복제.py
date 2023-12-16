'''
1. 복제마법 시전(복제는 모든 과정이 끝난 뒤 나타난다.)
2. 모든 물고기 한 칸 이동.
    2-0. 물고기는 상하좌우대각선 중 한 방향으로 이동
    2-1. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자를 벗어나는 칸으로는 이동 불가
    2-2. 만약 이동가능한 칸이 없으면 이동 x
3. 상어가 연속해서 세 칸 이동.
    3-1. 현재 칸에서 상하좌우로 인접한 칸으로 이동 가능
    3-2. 연속해서 이동하는 중에 물고기가 있는 칸으로 간다면 그 칸의 물고기는 격자에서 제외되고 냄새를 남긴다.

    : 가능한 이동방법 중에서
        1. 제외되는 물고기의 수가 가장 많은 방법
        2. 사전 순으로 가장 앞서는 방법
4. 두번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라짐
    -> 물고기가 냄새를 남기면 2로 초기화
5. 복제마법 실행. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖는다.
    - 이동한 위치가 아니다.

s번 연습을 모두 마쳤을 때 남아있는 물고기의 수 구하기
'''

from collections import deque
import sys, copy
input = sys.stdin.readline

def move_fish(shark_r, shark_c):
    global grounds
    temp_grounds = list()
    for r in range(1, 5):
        for c in range(1, 5):
            for idx in range(1, 9):
                if grounds[r][c][idx]:
                    direction = idx
                    orig_direction = direction
                    for _ in range(8):
                        cr = r + dr[direction]
                        cc = c + dc[direction]
                        # 범위 내에 있으면서 상어도 없고 냄새도 없다면
                        if 1 <= cr <= 4 and 1 <= cc <= 4 and (cr != shark_r or cc != shark_c) and smell[cr][cc] == 0:
                            temp_grounds.append([cr, cc, direction, grounds[r][c][idx]])
                            break
                        else:
                            direction -= 1
                            if direction <= 0:
                                direction += 8
                    # 그 자리에 있기
                    else:
                        temp_grounds.append([r, c, orig_direction, grounds[r][c][idx]])

    grounds = [[[0] * 9 for _ in range(5)] for _ in range(5)]
    for tr, tc, tdirection, num in temp_grounds:
        grounds[tr][tc][tdirection] += num
    return

#     0 좌 좌상 상 우상 우 우하 하 좌하
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 0, 상 좌 하 우
shark_dr = [0, -1, 0, 1, 0]
shark_dc = [0, 0, -1, 0, 1]

M, S = map(int, input().split())
grounds = [[[0] * 9 for _ in range(5)] for _ in range(5)]
smell = [[0] * 5 for _ in range(5)]
for _ in range(M):
    r, c, d = map(int, input().split())
    grounds[r][c][d] += 1

shark_r, shark_c = map(int, input().split())

for idx in range(1, S + 1):

    # 1. 상어가 모든 물고기에 복제 마법 시전
    copy_list = [[[0] * 9 for _ in range(5)] for _ in range(5)]
    for r in range(1, 5):
        for c in range(1, 5):
            for i in range(1, 9):
                copy_list[r][c][i] = grounds[r][c][i]

    # 2. 모든 물고기가 한 칸 이동
    move_fish(shark_r, shark_c)

    # 3. 상어가 연속해서 3칸 이동한다. 가장 물고기를 많이 먹을 수 있는 방법으로 이동
    # 경우의 수가 많다면 사전 순으로
    choice = list()
    maximum = 0
    temp_shark_r = 0
    temp_shark_c = 0

    temp_grounds_list = [[[0] * 9 for _ in range(5)] for _ in range(5)]
    for r in range(1, 5):
        for c in range(1, 5):
            for i in range(1, 9):
                temp_grounds_list[r][c][i] = grounds[r][c][i]

    for i in range(1, 5):
        cr1 = shark_r + shark_dr[i]
        cc1 = shark_c + shark_dc[i]
        if cr1 <= 0 or cr1 >= 5 or cc1 <= 0 or cc1 >= 5:
            continue
        sum1 = sum(temp_grounds_list[cr1][cc1])
        temp_grounds_list[cr1][cc1] = [0] * 9
        for j in range(1, 5):
            cr2 = cr1 + shark_dr[j]
            cc2 = cc1 + shark_dc[j]
            if cr2 <= 0 or cr2 >= 5 or cc2 <= 0 or cc2 >= 5:
                continue
            sum2 = sum(temp_grounds_list[cr2][cc2])
            temp_grounds_list[cr2][cc2] = [0] * 9
            for k in range(1, 5):
                cr3 = cr2 + shark_dr[k]
                cc3 = cc2 + shark_dc[k]
                if cr3 <= 0 or cr3 >= 5 or cc3 <= 0 or cc3 >= 5:
                    continue

                sum3 = sum(temp_grounds_list[cr3][cc3])
                # 물고기 최대로 많이 먹을 수 있는 방법
                if sum1 + sum2 + sum3 > maximum:
                    maximum = sum1 + sum2 + sum3
                    choice = [[cr1, cc1], [cr2, cc2], [cr3, cc3]]
                    temp_shark_r = cr3
                    temp_shark_c = cc3

                # 물고기 못먹을 때 방지
                if choice == []:
                    choice = [[cr1, cc1], [cr2, cc2], [cr3, cc3]]
                    temp_shark_r = cr3
                    temp_shark_c = cc3
            for i in range(1, 9):
                temp_grounds_list[cr2][cc2][i] = grounds[cr2][cc2][i]
        for i in range(1, 9):
            temp_grounds_list[cr1][cc1][i] = grounds[cr1][cc1][i]

    shark_r = temp_shark_r
    shark_c = temp_shark_c

    # 상어 이동, 물고기 제거됐다면 냄새를 남긴다.
    for cr, cc in choice:
        if sum(grounds[cr][cc]) > 0:
            # 물고기 먹기
            grounds[cr][cc] = [0] * 9
            smell[cr][cc] = idx

    # 4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
    for r in range(1, 5):
        for c in range(1, 5):
            if smell[r][c] + 2 <= idx:
                smell[r][c] = 0

    # 5.1에서 사용한 복제 마법이 완료된다.
    for r in range(1, 5):
        for c in range(1, 5):
            for i in range(1, 9):
                grounds[r][c][i] += copy_list[r][c][i]


# 숫자 세기
result = 0
for r in range(1, 5):
    for c in range(1, 5):
        for k in range(1, 9):
            result += grounds[r][c][k]

print(result)