'''
무방향 그래프
1번 정점에서 N번 정점으로 최단 거리로 이동하고자 한다.

임의의 주어진 두 정점은 반드시 통과해야 한다.

한번 이동했던 간선도 다시 이동할 수 있다. -> visited 사용 필요 x

'''

from collections import deque
import heapq, sys
input = sys.stdin.readline


def dijkstra(start, end, sweight):
    pq = []
    heapq.heappush(pq, (sweight, start))
    costs = [int(1e9)] * (N + 1)

    cnt = 0
    while pq:
        d, u = heapq.heappop(pq)
        cnt += 1
        if u == end:
            return d
        for v, w in graph[u]:
            nw = d + w
            if nw < costs[v]:
                costs[v] = nw
                heapq.heappush(pq, (nw, v))

    return -1


N, M = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    # 무방향 그래프
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())

# 출발지부터 도착지 경로가 존재하지 않는 경우
if dijkstra(1, N, 0) == -1:
    print(-1)
else:
    # 시작점 -> v1 -> v2 -> end
    total_1 = dijkstra(1, v1, 0) + dijkstra(v1, v2, 0) + dijkstra(v2, N, 0)
    # 시작점 -> v2 -> v1 -> end
    total_2 = dijkstra(1, v2, 0) + dijkstra(v2, v1, 0) + dijkstra(v1, N, 0)

    print(min(total_1, total_2))