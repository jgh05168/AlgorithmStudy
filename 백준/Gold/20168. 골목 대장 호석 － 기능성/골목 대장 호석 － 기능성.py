'''
양방향, 두 교차로를 잇는 골목은 한 개만 존재
수금 : weight

heapq : (수치심 정보, v)
'''

import sys, heapq
input = sys.stdin.readline


def move(start, end, coin):
    pq = []
    heapq.heappush(pq, (0, start, 0))
    visited = [0] * (n + 1)

    while pq:
        max_pay, u, used_coin = heapq.heappop(pq)
        visited[u] = 1
        if u == end:
            return max_pay
        for v, pay in graph[u]:
            if not visited[v]:
                if used_coin + pay > coin:
                    continue
                heapq.heappush(pq, (max(max_pay, pay), v, used_coin + pay))

    return -1


n, m, a, b, c = map(int, input().split())
graph = [[] * i for i in range(n + 1)]
for _ in range(m):
    su, sv, sw = map(int, input().split())
    graph[su].append((sv, sw))
    graph[sv].append((su, sw))

print(move(a, b, c))