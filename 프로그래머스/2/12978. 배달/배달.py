'''
양방향 그래프
시간 존재
1번 마을에 있는 음식점에서 각 마을로 배달
n개 마을 중 k시간 이하로 배달이 가능한 마을에서만 주문받는다.

bfs
'''
import sys, heapq

input = sys.stdin.readline


def bfs(su, graph, N, K):
    pq = []
    heapq.heappush(pq, (0, su))
    visited = [0] * N
    visited[su] = 1

    while pq:
        w, u = heapq.heappop(pq)
        visited[u] = 1
        for v, nw in graph[u]:
            if not visited[v] and w + nw <= K:
                heapq.heappush(pq, (w + nw, v))

    return sum(visited)


def solution(N, road, K):
    graph = [[] * N for _ in range(N)]
    for su, sv, sw in road:
        graph[su - 1].append((sv - 1, sw))
        graph[sv - 1].append((su - 1, sw))

    answer = bfs(0, graph, N, K)

    return answer