'''
빈 칸 0, 집 1, 치킨집 2
치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리 : 모든 집의 치킨 거리의 합

도시의 치킨거리를 최대한 작게 하기.

- 치킨집, 도시 좌표 구하기
- 집의 개수는 2N개를 넘지 않으며 적어도 1개는 존재한다.

- 백트래킹
'''

import sys
input = sys.stdin.readline


def dfs(cnt, road):
    global min_v

    if cnt == M:
        min_v = min(min_v, road)
        return


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

min_v = int(1e9)
# 먼저 도시, 치킨집 위치 찾기
chickens = []
cities = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            cities.append((i, j))
        elif grid[i][j] == 2:
            chickens.append((i, j))


# 가능한 비트마스킹
chicken_list = []
for i in range(1 << len(chickens)):
    temp = []
    for j in range(len(chickens)):
        if i & (1 << j):
            temp.append(chickens[j])
    chicken_list.append(temp)

chicken_list.sort(key=lambda x: len(x))

for idx in range(1, len(chicken_list)):
    chicken_cnts = len(chicken_list[idx])
    if chicken_cnts > M:
        break
    home_dist = [int(1e9)] * len(cities)
    temp_list = chicken_list[idx]

    for row, col in temp_list:
        for cidx in range(len(home_dist)):
            home_dist[cidx] = min(home_dist[cidx], abs(cities[cidx][0] - row) + abs(cities[cidx][1] - col))

    if sum(home_dist) < min_v:
        min_v = sum(home_dist)

print(min_v)