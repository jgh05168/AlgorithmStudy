'''
X번 마을에 모여서 파티를 하기로 함
단방향그래프, 간선과 가중치가 주어진다.
파티에 갔다가 자신들의 마을로 돌아와야 하는데 최단시간!

정답 : 오고 가는 길에 가장 많은 시간을 소비하는 학생을 찾아라.

문제풀이 : 파티장소에 갔다가 원래로 돌아오는 경우에 대한 다익스트라를 각각 구한 다음에 더해주는 방식
알고리즘 : 다익스트라

1000log1000
'''

import heapq, sys
input = sys.stdin.readline


def dijkstra(from_, to_, sd):
    path = [int(1e9)] * (N + 1)
    pq = []
    heapq.heappush(pq, (sd, from_))
    path[from_] = 0

    while pq:
        d, u = heapq.heappop(pq)

        if u == to_:
            return d

        if path[u] < d:
            continue

        for v, w in graph[u]:
            nw = w + d
            if path[v] > nw:
                path[v] = nw
                heapq.heappush(pq, (nw, v))


N, M, X = map(int, input().split())
# 인접리스트
graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

ans = 0
for student in range(1, N + 1):
    if student == X:
        continue
    ans = max(ans, dijkstra(student, X, 0) + dijkstra(X, student, 0))

print(ans)