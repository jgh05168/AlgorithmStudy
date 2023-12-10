'''
현재 위치에서 갈 수 있는 좌표 배열을 저장할 grid 생성
불이 켜진 지 아닌 지 확인하는 grid 생성

이미 켜져있다면 안켜도 된다.
'''

from collections import deque
import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol):
    light_on[srow][scol] = 1
    queue = deque()
    queue.append((srow, scol))
    lights = 1
    visited[srow][scol] = 1

    while queue:
        row, col = queue.popleft()

        while switch_locs[row][col]:
            nrow, ncol = heapq.heappop(switch_locs[row][col])
            if not light_on[nrow][ncol]:
                lights += 1
                light_on[nrow][ncol] = 1
                # 도달할 수 있는 위치인지 확인
                for d in range(len(dr)):
                    nnrow, nncol = nrow + dr[d], ncol + dc[d]
                    # 만약 이미 방문한 곳이라면 queue에 삽입
                    if 0 <= nnrow < n and 0 <= nncol < n and visited[nnrow][nncol]:
                        queue.append((nnrow, nncol))

        # 현재 위치를 기준으로 다시 검사
        # 초기 위치부터 다시 검사하게 되므로 스위치가 있는 목적지까지 큐에 계속 넣어볼 수 있음
        for d in range(len(dr)):
            nr, nc = row + dr[d], col + dc[d]
            # 첫 방문인데 이미 불이 켜져있다면 이동할 수 있는 곳임을 뜻함
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and light_on[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = 1

    return lights

n, m = map(int, input().split())
switch_locs = [[0] * n for _ in range(n)]
light_on = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y, a, b = map(int, input().split())
    if not switch_locs[x - 1][y - 1]:
        switch_locs[x - 1][y - 1] = [(a - 1, b - 1)]
    else:
        heapq.heappush(switch_locs[x - 1][y - 1], (a - 1, b - 1))

print(bfs(0, 0))