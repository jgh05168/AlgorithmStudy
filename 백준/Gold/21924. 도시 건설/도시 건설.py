'''
양방향 그래프
비용이 존재함

공사하는데 드는 비용을 최소한으로 하고자 함
모든 도로 연결되어야 함
== MST

최소 간선 사용해서 구하기 : 프림 알고리즘 사용
    - weight 낮은 순으로 저장
    - 만약 이미 방문한 곳이라면 continue 처리
'''

import sys, heapq
input = sys.stdin.readline

def prim(scity):
    global used_weight
    pq = []
    for sw, sv in city[scity]:
        heapq.heappush(pq, (sw, sv))
    visited[scity] = 1
    while pq:
        w, u = heapq.heappop(pq)
        # 만약 이미 방문한 곳이라면 continue
        if visited[u]:
            continue
        visited[u] = 1
        used_weight += w

        for nw, v in city[u]:
            if not visited[v]:
                heapq.heappush(pq, (nw, v))

    return total_weight - used_weight


n, m = map(int, input().split())
city = [[] * n for _ in range(n)]
total_weight = 0        # 총 가중치
used_weight = 0         # 구해야 할 가중치

for _ in range(m):
    # weight와 현재 노드, 다음 노드 정보를 저장
    u, v, w = map(int, input().split())
    city[u - 1].append((w, v - 1))
    city[v - 1].append((w, u - 1))
    total_weight += w

visited = [0] * n
prim(0)
if sum(visited) != n:
    print(-1)
else:
    print(total_weight - used_weight)