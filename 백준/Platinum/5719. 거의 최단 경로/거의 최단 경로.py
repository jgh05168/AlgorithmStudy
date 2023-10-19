'''

먼저 최단경로를 찾으면 continue. 이후 나오는 최단경로보다 값이 큰 경로에 대해 출력.
단방향 그래프이지만 최단경로를 알기 위한 역방향그래프도 필요하다.

1. 최단경로를 먼저 계산. 
2. bfs를 사용하여 최단경로였던 길에 대해서 체크해준다.
    1. 이전 노드의 가중치 + 이전 노드의 최단경로값 == 현재 노드의 최단경로값
    2. 아직 방문하지 않은 지점일 경우
    
    위 2가지 조건을 만족할 경우에 최단경로에 포함된다.
    
3. 후 다시 dijkstra를 돌린다.
'''


from collections import deque
import sys, heapq
input = sys.stdin.readline

def dijkstra(S):
    global shortest_path
    pq = []
    heapq.heappush(pq, (0, S))
    visited = [INF] * N
    visited[S] = 0
    shortest_cost = int(1e9)

    while pq:
        cur_cost, u = heapq.heappop(pq)
        if u == D:
            continue
        if shortest_cost < cur_cost:
            break
        for v, w in graph[u]:
            if edges[u][v]:
                continue
            new_cost = cur_cost + w
            if visited[v] > new_cost:
                visited[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return visited


# 역으로 최단거리 찾기
def bfs(d):
    queue = deque()
    queue.append(d)

    while queue:
        u = queue.popleft()

        if u == S:
            continue

        for v, w in reversed_graph[u]:
            # 만약 이전 노드 최단거리 + 이전 노드의 가중치가 현재 노드의 가중치와 같고, 아직 방문하지 않았다면,
            # 최단거리의 경로에 포함된다.
            if shorted_paths[v] + w == shorted_paths[u] and not edges[v][u]:
                edges[v][u] = 1         # 방문표시
                queue.append(v)


while True:
    N, M = map(int, input().split())
    if not N and not M:
        break

    S, D = map(int, input().split())
    graph = [[] * N for _ in range(N)]              # 정방향 그래프
    reversed_graph = [[] * N for _ in range(N)]     # 역방향 그래프
    edges = [[0] * N for _ in range(N)]             # 최단거리를 역방향에서 시작하여 체크하기
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        reversed_graph[v].append((u, w))

    INF = int(1e9)
    shorted_paths = dijkstra(S)
    bfs(D)
    ans_paths = dijkstra(S)

    if ans_paths[D] == INF:
        print(-1)
    else:
        print(ans_paths[D])

