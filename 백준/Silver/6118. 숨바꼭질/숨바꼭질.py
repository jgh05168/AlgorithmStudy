'''양방향 길
냄새는 1번 헛간에서의 거리가 멀어질수록 감소한다.
만약 거리가 같읜 헛간이라면 가장 작은 헛간 번호를 출력한다.

'''

from collections import deque
import sys
input = sys.stdin.readline


# 1번 헛간까지의 거리만 계산해주면 된다
def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = visited[node] + 1
                queue.append(i)


n, m = map(int, input().split())
graph = [[] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
visited = [0] * n

bfs(0)
ans = max(visited)

print(visited.index(ans) + 1, ans - 1, visited.count(ans))