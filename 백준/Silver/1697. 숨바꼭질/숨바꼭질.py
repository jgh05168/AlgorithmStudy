from collections import deque

dd = [1, -1]

def bfs(s):
    visited = [-1] * 100001
    visited[s] = 0
    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()

        for d in range(len(dd)):
            v = u + dd[d]
            if 0 <= v <= 100000 and visited[v] == -1:
                if v == K:
                    return visited[u] + 1
                visited[v] = visited[u] + 1
                queue.append(v)

        v = u * 2
        if 0 <= v <= 100000 and visited[v] == -1:
            if v == K:
                return visited[u] + 1
            visited[v] = visited[u] + 1
            queue.append(v)



N, K = map(int, input().split())
if N == K:
    print(0)
else:
    print(bfs(N))