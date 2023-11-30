'''
감염을 맵에는 표시, visited에는 시간 정보를 저장
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(virus_village):
    queue = virus_village

    while queue:
        virus_num, row, col, time = queue.popleft()

        if villages[row][col] == 3:     # 이후 과정에서 3번 바이러스로 변했다면 continue
            continue

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and villages[nrow][ncol] != -1:
                # 만약 현재 마을과 감염된 마을이 같거나 이미 두군데 모두에게 감염되었다면 continue
                if villages[nrow][ncol] == virus_num or villages[nrow][ncol] == 3:
                    continue
                # 아직 감염되지 않은 경우
                if not villages[nrow][ncol]:
                    villages[nrow][ncol] = virus_num
                    visited[nrow][ncol] = time + 1
                    queue.append((virus_num, nrow, ncol, time + 1))
                # 감염된 곳이라면
                else:
                    # 시간이 지나지 않았다면
                    if visited[nrow][ncol] == time + 1:
                        villages[nrow][ncol] += virus_num


n, m = map(int, input().split())
villages = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

virus_village = deque()
for i in range(n):
    for j in range(m):
        if villages[i][j] == -1:
            continue
        if villages[i][j]:
            virus_village.append((villages[i][j], i, j, 0))
            visited[i][j] = 0

bfs(virus_village)

one, two, three = 0, 0, 0
for i in range(n):
    for j in range(m):
        if villages[i][j] == 1:
            one += 1
        elif villages[i][j] == 2:
            two += 1
        elif villages[i][j] == 3:
            three += 1
print(one, end=' ')
print(two, end=' ')
print(three)
