import heapq

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dijkstra(srow, scol):
    queue = []
    heapq.heappush(queue, (0, srow, scol))
    path[srow][scol] = 0
    while queue:
        cost, row, col = heapq.heappop(queue)
        height = city[row][col]
        if (row, col) == (N - 1, N - 1):
            return cost
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]

            if 0 <= nrow < N and 0 <= ncol < N:
                new_cost = cost + city[nrow][ncol]

                if new_cost < path[nrow][ncol]:
                    heapq.heappush(queue, (new_cost, nrow, ncol))
                    path[nrow][ncol] = new_cost


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    city = [list(map(int, input())) for _ in range(N)]
    path = [[int(1e9)] * N for _ in range(N)]

    min_cost = dijkstra(0, 0)
    print(f'#{tc} {min_cost}')