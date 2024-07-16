'''
특정한 위치에 바이러스 존재 가능

번호가 낮은 종류의 바이러스부터 먼저 증식한다.
증식 과정에서 이미 바이러스가 존재한다면, 다른 바이러스는 들어갈 수 없음

풀이 :

heapq 사용.

heapq로 돌고, for문으로 시간 돌면서 업데이트 해주면 될 듯
'''

import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def multiplication(pq):
    tmp_pq = []

    while pq:
        num, row, col = heapq.heappop(pq)

        for d in range(len(dr)):
            nr, nc = row + dr[d], col + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:
                grid[nr][nc] = num
                heapq.heappush(tmp_pq, (grid[nr][nc], nr, nc))

    return tmp_pq


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

pq = []
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            heapq.heappush(pq, (grid[i][j], i, j))

for _ in range(s):
    pq = multiplication(pq)

print(grid[x - 1][y - 1])