'''
단방향그래프

다익스트라

'''

import sys, heapq
input = sys.stdin.readline

def dijkstra(su):
    visited = [int(1e9)] * n
    visited[su] = 0
    pq = []
    heapq.heappush(pq, (0, su))

    while pq:
        w, u = heapq.heappop(pq)

        if u == end - 1:
            return w
        for v, nw in graph[u]:
            new_w = w + nw
            if new_w < visited[v]:
                visited[v] = new_w
                heapq.heappush(pq, (new_w, v))


n = int(input())
m = int(input())
graph = [[] * n for _ in range(n)]
for _ in range(m):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b - 1, l))
start, end = map(int, input().split())


ans = dijkstra(start - 1)

if ans == None:
    print(0)
else:
    print(ans)