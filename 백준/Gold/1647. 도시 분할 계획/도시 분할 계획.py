'''
MST

최소 유지비(weight)를 얻기 위해서는
 -> MST를 구한 후 가장 큰 가중치의 값을 빼주면 된다.

'''


import heapq
import sys
input = sys.stdin.readline


############# Prim's Algorithm ####################
# def prim(start):
#     pq = []
#     heapq.heappush(pq, (0, start))
#
#     total = 0
#     max_w = 0
#     while pq:
#         d, u = heapq.heappop(pq)
#
#         if visited[u]:
#             continue
#
#         total += d
#         if max_w < d:
#             max_w = d
#         visited[u] = 1
#
#         for v, w in houses[u]:
#             if not visited[v]:
#                 heapq.heappush(pq, (w, v))
#
#
#     return total - max_w
#
# N, M = map(int, input().split())
# houses = [[] * (N + 1) for _ in range(N + 1)]
# visited = [0] * (N + 1)
# for _ in range(M):
#     u, v, w = map(int, input().split())
#     houses[u].append((v, w))
#     houses[v].append((u, w))
#
# print(prim(1))


############# Kruskal's Algorithm ####################

def find_set(x):
    if houses[x] != x:
        houses[x] = find_set(houses[x])
    return houses[x]


def union(x, y):
    x, y = find_set(x), find_set(y)

    # 사이클 발생 확인해주기
    if x == y:
        return

    if x < y:
        houses[y] = x
    else:
        houses[x] = y


N, M = map(int, input().split())
roads = []
for _ in range(M):
    u, v, w = map(int, input().split())
    roads.append((u, v, w))

roads.sort(key=lambda x: x[2])      # 가중치 값에 대해 오름차순으로 정렬

houses = [i for i in range(N + 1)]

# Kruskal
visited = 0
total = 0
max_w = 0
for u, v, w in roads:
    # 사이클이 발생하지 않는다면 집합 생성
    if find_set(u) != find_set(v):
        union(u, v)
        total += w
        if max_w < w:
            max_w = w
        if visited == N:
            break

print(total - max_w)
