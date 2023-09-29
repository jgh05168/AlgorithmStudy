'''
MST

Prim's Algorithm 으로 구현
heapq, 인접리스트 사용
'''


import heapq, sys
input = sys.stdin.readline


def prim(start, sweight):
    pq = []
    heapq.heappush(pq, (sweight, start))

    weight_sum = 0
    visit_num = 0
    while pq:
        w, u = heapq.heappop(pq)

        # 모든 구간을 방문했다면, 종료
        if visit_num == V:
            break
        # 이미 방문한 곳이라면
        if visited[u]:
            continue

        # 방문 표시
        visited[u] = 1
        visit_num += 1
        # 가중치 업데이트
        weight_sum += w

        for v, nw in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (nw, v))

    return weight_sum

V, E = map(int, input().split())
graph = [[] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [0] * (V + 1)
print(prim(1, 0))