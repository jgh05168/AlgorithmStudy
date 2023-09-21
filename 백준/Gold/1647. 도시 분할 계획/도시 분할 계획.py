'''
MST - Prim's Algorithm with heapq

최소 유지비(weight)를 얻기 위해서는
 -> MST를 구한 후 가장 큰 가중치의 값을 빼주면 된다.

'''


import heapq
import sys
input = sys.stdin.readline

def prim(start):
    pq = []
    heapq.heappush(pq, (0, start))

    total = 0
    max_w = 0
    while pq:
        d, u = heapq.heappop(pq)

        if visited[u]:
            continue

        total += d
        if max_w < d:
            max_w = d
        visited[u] = 1

        for v, w in houses[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))


    return total - max_w

N, M = map(int, input().split())
houses = [[] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v, w = map(int, input().split())
    houses[u].append((v, w))
    houses[v].append((u, w))

print(prim(1))