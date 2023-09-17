'''
최단 경로 : 가중치가 주어진 경우

- 대표적인 Dijkstra 알고리즘

- visited 배열에 가중치 값에 대해서 저장한다.
- "힙을 사용한 우선순위큐 사용"
    -> heapq : 데이터의 첫번째 값에 대해 오름차순으로 정렬된 큐
    -> 우선순위 큐를 이용하게 되면 우선순위 큐가 알아서 가장 최단 거리인 노드를 가장 앞으로 정렬해준다
    = 기존에 기록한 최단 거리보다 크다면 그냥 무시해주면 된다.
    if, 현재 거리가 기존 최단거리보다 짧다면 :
        해당 거리와 노드를 우선순위 큐에 넣어준다.
'''

import sys, heapq
input = sys.stdin.readline

def dijkstra(u):
    queue = []
    # 우리는 가중치가 낮은 순으로 정렬할 것이기 때문에 가중치가 맨 앞에 위치해야 한다.
    heapq.heappush(queue, (0, u))   # (현재 노드의 가중치, 현재 노드)
    shortest_paths[u] = 0
    while queue:
        weight, u = heapq.heappop(queue)
        if shortest_paths[u] < weight:       # 만약 가중치가 이미 저장된 값보다 클 경우 무시
            continue
        else:
            for v, w in graph[u]:
                cost = weight + w
                if cost < shortest_paths[v]:
                    shortest_paths[v] = cost
                    heapq.heappush(queue, (cost, v))


V, E = map(int, input().split())
start_v = int(input())
graph = [[] * V for _ in range(V + 1)]
shortest_paths = [int(1e9)] * (V + 1)           # 다익스트라 알고리즘의 초기 가중치는 무한대로 설정
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start_v)

for i in range(1, V + 1):
    if shortest_paths[i] == int(1e9):
        print('INF')
    else:
        print(shortest_paths[i])