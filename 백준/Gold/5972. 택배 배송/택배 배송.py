'''
최소한의 소를 만나면서 지나가기

양방향 그래프

dijkstra
'''

import heapq, sys
input = sys.stdin.readline


def dijkstra(su):
    pq = []
    heapq.heappush(pq, (0, su))

    while pq:
        cur_w, u = heapq.heappop(pq)

        if u == n:
            return cur_w

        for v, w in graph[u]:
            if cur_w + w < visited[v]:
                visited[v] = cur_w + w
                heapq.heappush(pq, (cur_w + w, v))

    return -1

n, m = map(int, input().split())
graph = [[] * i for i in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

visited = [int(1e9)] * (n + 1)
print(dijkstra(1))