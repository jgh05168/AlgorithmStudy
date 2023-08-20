N, M, V = map(int, input().split())
graph = [[] * N for _ in range(N + 1)]      # 빈 그래프 생성
# 순서 저장을 위한 빈 리스트
dfs_list = []
bfs_list = []

# graph 인접리스트 생성
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 그래프 내부 인접리스트들을 오름차순으로 정렬
for i in range(1, N + 1):
    graph[i].sort()

def bfs(s, bfs_list):
    queue = []
    visited = [False] * (N + 1)
    visited[s] = True
    queue.append(s)

    while queue:
        v = queue.pop(0)
        bfs_list.append(v)
        for w in graph[v]:
            if visited[w] == False:
                queue.append(w)
                visited[w] = True

def dfs(v, dfs_list):
    if visited_dfs[v]:
        return
    else:
        visited_dfs[v] = True
        dfs_list.append(v)
        for w in graph[v]:
            if not visited_dfs[w]:
                dfs(w, dfs_list)

bfs(V, bfs_list)
visited_dfs = [False] * (N + 1)
dfs(V, dfs_list)

print(*dfs_list)
print(*bfs_list)