def bfs(city):
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
                    if w == chickens[0] or w == chickens[1]:
                        return visited[v]
                    else:
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
for i in range(1, N):
    for j in range(i + 1, N + 1):
        chickens = (i, j)
        total_dist = 0
        for city in range(1, N + 1):
            total_dist += 2 * bfs(city)
        dist.append([i, j, total_dist])

dist.sort(key=lambda x: x[2])
print(*dist[0])