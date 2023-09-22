'''
방향그래프, 가중치 정보가 있다.

dijkstra 두 번 돌면 해결될 것 같은데

'''

import heapq

def dijkstra(su, dest):
    global min_cost
    pq = []
    heapq.heappush(pq, (0, su))
    costs = [int(1e9)] * (N + 1)
    costs[su] = 0

    while pq:
        cw, u = heapq.heappop(pq)

        if u == dest:
            return cw

        for v, w in town[u]:
            nw = cw + w
            if nw < costs[v]:
                costs[v] = nw
                heapq.heappush(pq, (nw, v))


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())     # N : 집 개수, M : 연결정보, X : 인수 집

    town = [[] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        # x번 집에서 y번 집으로 가는 데 시간이 c가 걸리는 단 방향 도로가 존재
        x, y, c = map(int, input().split())
        town[x].append((y, c))

    max_cost = 0
    for i in range(1, N + 1):
        total_cost = 0
        if i != X:
            total_cost = dijkstra(i, X) + dijkstra(X, i)
            if max_cost < total_cost:
                max_cost = total_cost

    print(f'#{tc} {max_cost}')