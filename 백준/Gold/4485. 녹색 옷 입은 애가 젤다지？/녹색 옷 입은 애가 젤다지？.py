'''
단순 dijkstra
루피가 작은 쪽으로만 이동하면 된다.
'''

import heapq, sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dijkstra(srow, scol):
    pq = []
    heapq.heappush(pq, (cave[srow][scol], srow, scol))
    visited = [[int(1e9)] * N for _ in range(N)]
    visited[srow][scol] = cave[srow][scol]

    while pq:
        cur_cost, row, col = heapq.heappop(pq)

        if (row, col) == (N - 1, N - 1):
            return cur_cost

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N:
                new_cost = cur_cost + cave[nrow][ncol]
                if visited[nrow][ncol] > new_cost:
                    visited[nrow][ncol] = new_cost
                    heapq.heappush(pq, (new_cost, nrow, ncol))

tc = 1
while True:
    N = int(input())
    if not N:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {tc}: {dijkstra(0, 0)}')
    tc += 1