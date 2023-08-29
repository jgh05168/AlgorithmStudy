def bfs(city):
    # 만약 현재 노드가 치킨집이면 거리 0 반환
    if city == chickens[0] or city == chickens[1]:
        return 0
    else:
        visited = [0] * (N + 1)
        queue = [city]
        visited[city] = 1
        while queue:
            v = queue.pop(0)
            for w in graph[v]:
                if not visited[w]:
                    # 만약 인접한 도시가 치킨집이라면
                    if w == chickens[0] or w == chickens[1]:
                        return visited[v]   # 현재 거리만큼 반환
                        # 어떻게든 탐색이 될것이기 떄문에 반환이 안될 리는 없다.
                    else:   # 아니라면 일반 bfs 수행
                        queue.append(w)
                        visited[w] = visited[v] + 1


min_time = 100000000
N, M = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)


dist = []
# 가능한 치킨집 모두 탐색(순열처럼)
for i in range(1, N):
    for j in range(i + 1, N + 1):
        chickens = (i, j)
        total_dist = 0
        # 도시를 하나씩 탐색하며 치킨집과의 거리 bfs로 계산
        for city in range(1, N + 1):
            total_dist += 2 * bfs(city)     # 왕복거리이기 때문에 *2

        # 현재 좌표, 모든 도시에서 치킨집까지의 왕복 거리를 리스트에 저장
        dist.append([i, j, total_dist])

dist.sort(key=lambda x: x[2])
print(*dist[0])
