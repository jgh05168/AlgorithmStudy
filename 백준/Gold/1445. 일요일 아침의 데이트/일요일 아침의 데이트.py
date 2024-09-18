'''
1. 쓰레기를 통과해서 지나가는걸 정말 싫어한다.
2. 쓰레기를 따라 옆을 지나가는 것도 불편하게 느낀다.

쓰레기로 차있는 칸을 되도록이면 적게 지나가고자 한다.
최적의 방법으로 숲을 지났을 때, 지나가는 쓰레기의 최소 개수와 쓰레기 옆을 지나가는 칸의 개수를 출력

풀이:
bfs
visited 배열에 쓰레기 칸을 지난 경우 & 인접 쓰레기를 지난 경우에 대한 정보를 저장한다.
이후 값을 비교해가며 최소인 부분에 대해서만 이동할 수 있도록 한다.
'''

import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr, sc):
    global ans1, ans2
    pq = []

    visited[sr][sc] = (0, 0)
    heapq.heappush(pq, (0, 0, sr, sc))

    while pq:
        g, adj_g, r, c = heapq.heappop(pq)

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                # 도착점에 도착한 경우
                if grid[nr][nc] == 'F':
                    return g, adj_g
                # 현재 위치에서 쓰레기와 인접 쓰레기 가지수를 체크
                new_g, new_adj_g = g, adj_g
                if grid[nr][nc] == 'g':
                    new_g = g + 1
                elif grid[nr][nc] == '.':
                    new_adj_g = adj_g + adj_garbage[nr][nc]
                # 이동 가능한 경우 : (nr, nc)가 모두 현재보다 작은 경우
                if visited[nr][nc][0] > new_g or (visited[nr][nc][0] == new_g and visited[nr][nc][1] > new_adj_g):
                    visited[nr][nc] = (new_g, new_adj_g)
                    heapq.heappush(pq, (new_g, new_adj_g, nr, nc))


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    try:
        sc = grid[i].index('S')
        sr = i
        break
    except:
        continue

visited = [[(250, 250)] * m for _ in range(n)]
adj_garbage = [[0] * m for _ in range(n)]
# 인접한 쓰레기가 있는 개수 세어주기
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            for d in range(len(dr)):
                ni, nj = i + dr[d], j + dc[d]
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 'g':
                    adj_garbage[i][j] = 1
                    break

print(*bfs(sr, sc))