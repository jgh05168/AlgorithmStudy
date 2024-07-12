'''
그냥 bfs
'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(su):
    queue = deque()
    queue.append(su)
    visited[su] = 1

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1


n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)