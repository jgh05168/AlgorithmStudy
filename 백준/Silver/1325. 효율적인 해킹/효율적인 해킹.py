'''
양방향 그래프

방문한 곳에 현재 위치에서 방문할 수 있는 거리 저장
'''

from collections import deque
import sys
input = sys.stdin.readline


def bfs(su):
    queue = deque()
    queue.append(su)
    visited = [0] * (n + 1)
    visited[su] = 1
    cnt = 1

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1
                cnt += 1
    return cnt


n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    su, sv = map(int, input().split())
    graph[sv].append(su)

max_cnt = 1
ans = []
for u in range(1, n + 1):
    cnt = bfs(u)
    if max_cnt < cnt:
        ans = []
        max_cnt = cnt
        ans.append(u)
    elif max_cnt == cnt:
        ans.append(u)

print(*ans)