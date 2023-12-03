'''
각 물고기는 번호와 방향(8가지)이 존재함

start point : (0, 0)
방향은 (0, 0)의 물고기 방향과 같다.

물고기는 번호가 작은 물고기부터 순서대로 이동한다.
이동가능 : 빈 칸 or 다른 물고기가 있는 칸
이동 불가 : 상어 or 공간 이외의 칸
각 물고기는 이동가능한 방향이 나올 때까지 반시계로 45도 씩 회전시킨다.
이동 불가능하면 이동 안하고 이동 가능하면 그 칸으로 이동
만약 다른 물고기가 존재한다면 서로 위치를 바꾸는 식

순서 : 물고기 이동 -> 상어 이동
상어는 한번에 여러 개의 칸을 이동할 수 있다. 물고기가 있다면 먹고 그 물고기의 방향을 가짐
이동 중 칸의 물고기는 먹지 않음
물고기가 없는 칸으로는 이동 불가.


dfs 진행 시 맵을 같이 넘겨주어야 한다.
상어의 이동에 따라서 재귀를 수행해주기
종료조건 : 상어가 이동을 못하는 경우
'''

import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(ocean, fish_info, shark, eaten_fish):
    global max_eaten_fish
    # 1. 상어가 현재 위치 물고기 먹기
    shark_row, shark_col = shark[0], shark[1]
    eaten_fish += (ocean[shark_row][shark_col][0] + 1)
    max_eaten_fish = max(max_eaten_fish, eaten_fish)
    fish_info[ocean[shark_row][shark_col][0]] = (-2, -2)
    ocean[shark_row][shark_col] = (-1, ocean[shark_row][shark_col][1])


    # 2. 물고기 이동
    for fish_idx in range(fish_cnt):
        if fish_info[fish_idx][0] == -1 or fish_info[fish_idx][0] == -2:
            continue
        row, col = fish_info[fish_idx][0], fish_info[fish_idx][1]
        # 방향 별 갈 수 있는 곳인지 확인.
        for d in range(len(dr)):
            nrow, ncol = row + dr[(ocean[row][col][1] + d) % 8], col + dc[(ocean[row][col][1] + d) % 8]
            if 0 <= nrow < n and 0 <= ncol < m and ocean[nrow][ncol][0] != -1:
                ocean[row][col] = (ocean[row][col][0], (ocean[row][col][1] + d) % 8)
                fish_info[fish_idx] = (nrow, ncol)
                if ocean[nrow][ncol][0] >= 0:
                    fish_info[ocean[nrow][ncol][0]] = (row, col)
                ocean[row][col], ocean[nrow][ncol] = ocean[nrow][ncol], ocean[row][col]
                break

    # 3. 상어 이동.
    # 가능한 모든 경우에 대해 탐색
    sshark_row, sshark_col = shark_row, shark_col
    shark_dir = ocean[shark_row][shark_col][1]
    while 0 <= shark_row + dr[shark_dir] < n and 0 <= shark_col + dc[shark_dir] < m:
        nshark_row = shark_row + dr[shark_dir]
        nshark_col = shark_col + dc[shark_dir]
        if ocean[nshark_row][nshark_col][0] != -2:
            tmp_ocean_info = ocean[nshark_row][nshark_col]
            ocean[sshark_row][sshark_col] = (-2, -2)
            dfs(copy.deepcopy(ocean), copy.deepcopy(fish_info), (nshark_row, nshark_col), eaten_fish)
            ocean[sshark_row][sshark_col] = (-1, shark_dir)
            ocean[nshark_row][nshark_col] = tmp_ocean_info
        shark_row, shark_col = nshark_row, nshark_col

    return


ocean = []
for _ in range(4):
    input_fishes = list(map(int, input().split()))
    tmp_infos = []
    for info in range(0, len(input_fishes), 2):
        tmp_infos.append((input_fishes[info] - 1, input_fishes[info + 1] - 1))
    ocean.append(tmp_infos)

fish_info = [0] * len(tmp_infos) * 4
for i in range(4):
    for j in range(len(tmp_infos)):
        fish_info[ocean[i][j][0]] = (i, j)

fish_cnt = len(fish_info)
eaten_fish = 0
max_eaten_fish = 0
# 상어가 바다에 들어감. (초기상태. 상어는 -1로 표기)
shark = (0, 0)
n, m = len(ocean), len(ocean[0])

dfs(ocean, fish_info, shark, 0)

print(max_eaten_fish)