'''
크기 n x m 지도, 오른쪽은 동쪽, 위는 북쪽

주사위는 윗면이 1, 동쪽을 바라보는 방향이 3인 상태로 놓여있음
    - 바닥 = 6
    - 서쪽 = 4

이동한 칸에 쓰여있는 수 = 0이면, 주사위의 바닥면에 쓰여있는 수가 칸에 복사된다.
0이 아인 경우에는 칸에 쓰여있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여있는 수는 0

주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램
- 만약 범위를 벗어난다면, 해당 명령을 무시하자. 출력도 하면 안된다.

풀이:
단순 시뮬

짝을 이루는 숫자 : [1, 6], [2, 5], [3, 4]
'''

import sys
input = sys.stdin.readline

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))    # 1: 동, 2: 서, 3: 북, 4: 남

dice_zzak = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}
dice_side = {0: (0, 2, 3, 1, 4),
             1: (0, 2, 3, 5, 0),
             2: (0, 5, 0, 1, 4),
             3: (0, 0, 5, 1, 4),
             4: (0, 2, 3, 0, 5),
             5: (0, 2, 3, 4, 1)}

dice = [0] * 6

down = 5
for order in orders:
    nx, ny = x + dr[order], y + dc[order]
    if not (0 <= nx < n and 0 <= ny < m):   # 이동 불가능한 경우
        continue
    # 동쪽
    if order == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 서쪽
    elif order == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 북쪽
    elif order == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    # 남쪽
    else:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
        
    if not maps[nx][ny]:
        maps[nx][ny] = dice[down]
    else:
        dice[down] = maps[nx][ny]
        maps[nx][ny] = 0
    print(dice[dice_zzak[down]])
    x, y = nx, ny