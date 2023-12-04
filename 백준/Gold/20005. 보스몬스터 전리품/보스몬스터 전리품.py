'''
한 칸씩 이동.

bfs

만약 보스에게 도착 시 보스의 체력을 깎기
딕셔너리 사용하여 값 저장
이동 먼저 진행하고 체력 깎기
이동했는지 여부는 따로 해시테이블 만들어 확인하기.
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(player_info):
    queue = player_info
    new_queue = deque()
    while queue:
        player, row, col = queue.popleft()
        player_idx = players_idx[player]

        if player in arrived:
            continue
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[player_idx][nrow][ncol] and field[nrow][ncol] != 'X':
                if field[nrow][ncol] == 'B':
                    arrived.add(player)
                    break
                visited[player_idx][nrow][ncol] = 1
                new_queue.append((player, nrow, ncol))

    return new_queue




n, m, player_cnt = map(int, input().split())
field = [list(input().rstrip()) for _ in range(n)]
players = {}
players_idx = {}
p = ord('a')
p_idx = 0
for _ in range(player_cnt):
    player, damage = input().split()
    players.update({player: int(damage)})
    players_idx.update({chr(p): p_idx})
    p += 1
    p_idx += 1

boss_hp = int(input())

# 초기 플레이어 위치 찾기
visited = [[[0] * m for _ in range(n)] for _ in range(player_cnt)]
player_info = []
for i in range(n):
    for j in range(m):
        if field[i][j].isalpha() and field[i][j].islower():
            player_info.append((field[i][j], i, j))


player_info.sort(key=lambda x: x[0])
arrived = set()
for pp, r, c in player_info:
    visited[players_idx[pp]][r][c] = 1

player_info = deque(player_info)
while boss_hp > 0:
    # 플레이어 이동
    tmp_queue = bfs(player_info)

    for p in arrived:
        boss_hp -= players[p]

    player_info = tmp_queue

print(len(arrived))