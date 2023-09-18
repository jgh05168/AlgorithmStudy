'''
선발명단

한 줄씩 백트래킹 시도.
- 값이 0이라면 건너뛰기
- 아니라면 일단 배열에 값 집어넣어
- 새로운 배열값이 들어오면 max를 비교하여 삽입

'''

import sys
input = sys.stdin.readline

def set_position(player, stat):
    global max_stat
    if player >= 11:
        if max_stat < stat:
            max_stat = stat
        return

    for i in range(len(stats)):
        if not stats[player][i]:
            continue
        else:
            if not players[player] and not positions[i]:
                players[player] = 1
                positions[i] = stats[player][i]
                set_position(player + 1, stat + stats[player][i])
                players[player] = 0
                positions[i] = 0


T = int(input())

for _ in range(T):
    players = [0] * 11
    positions = [0] * 11

    max_stat = 0
    stats = []
    for i in range(11):
        stats.append(list(map(int, input().split())))
    set_position(0, 0)

    print(max_stat)
