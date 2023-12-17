'''
bfs

보석이 있는 섬을 인덱스화 시켜주어 비트마스킹으로 visited에 넘겨준다.

'''

from collections import deque, defaultdict
import sys, copy
input = sys.stdin.readline


def bfs(su):
    global max_jewel

    queue = deque()
    # 현재 노드, 먹은 노드 수, 보석을 먹은 인덱스, 어떤 보석을 먹었는지 4가지 정보를 갖는다.
    queue.append((su, 0, 0, []))
    visited[0][su] = 1

    while queue:
        u, cur_jewel, v_idx, get_jewel = queue.popleft()

        for v, w in graph[u]:
            if not visited[v_idx][v] and cur_jewel <= w:
                if not v:
                    if treasure_check[v]:
                        max_jewel = max(max_jewel, cur_jewel + 1)
                    else:
                        max_jewel = max(max_jewel, cur_jewel)
                # 보석을 줍는 경우와 줍지 않는 경우를 나눠야 한다.
                else:
                    # 무조건 안줍고 지나가는 경우가 존재
                    queue.append((v, cur_jewel, v_idx, get_jewel))
                    visited[v_idx][v] = 1
                    # 보석이 존재한다면
                    if treasure_check[v]:
                        if v in get_jewel:      # 이미 먹은 보석인지 체크
                            continue
                        if cur_jewel <= w:
                            queue.append((v, cur_jewel + 1, v_idx + (1 << treasure_idx[v]), get_jewel + [v]))
                            visited[v_idx + (1 << treasure_idx[v])][v] = 1


n, m, k = map(int, input().split())
treasure_check = [0] * n
visited = [[0] * n for _ in range(1 << k)]
treasure_idx = defaultdict(int)
for i in range(k):
    treasure_island = int(input())
    treasure_check[treasure_island - 1] = 1 # 보석이 있는 섬인지 확인하는 용도
    treasure_idx[treasure_island - 1] = i       # 보석이 있는 섬의 번호를 인덱스화(visited의 인덱스로 활용)
graph = [[] for _ in range(n)]
for _ in range(m):
    # 양방향 그래프
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

max_jewel = 0
bfs(0)

print(max_jewel)