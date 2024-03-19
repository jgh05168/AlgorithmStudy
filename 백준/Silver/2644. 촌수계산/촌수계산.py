'''
트리 구조

풀이 :
1. dfs 탐색하며 visited에 저장
2. 저장된 idx값을 구해 절댓값 빼기를 진행한다.
3. 만약 둘 중 하나라도 방문하지 않았다면, -1 출력
'''

import sys
input = sys.stdin.readline


def dfs(u, cnt):
    global flag
    visited[u] = cnt
    if u == b:
        flag = 1
        print(cnt)
    for v in graph[u]:
        if not visited[v]:
            dfs(v, cnt + 1)


n = int(input())
a, b = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

flag = 0
dfs(a, 0)

if not flag:
    print(-1)
