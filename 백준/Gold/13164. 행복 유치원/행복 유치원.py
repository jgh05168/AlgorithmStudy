'''
일렬로 줄 세우고 K개의 조로 나누려고 한다.

- 정렬
- 그리디 & 백트래킹

'''

import sys, heapq
input = sys.stdin.readline


N, K = map(int, input().split())
children = list(map(int, input().split()))
children.sort()

lst = []
for i in range(N - 1):
    heapq.heappush(lst, (-(children[i + 1] - children[i]), i, i + 1))

idx_list = []
for i in range(K - 1):
    val, s, e = heapq.heappop(lst)
    idx_list.append(e)

idx_list.sort()

ans = 0
start = 0
for i in idx_list:
    ans += children[i - 1] - children[start]
    start = i
ans += children[-1] - children[start]

print(ans)
