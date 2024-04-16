'''
풀이:
N <= 10
백트래킹으로 충분히 풀이 가능
'''

import sys
input = sys.stdin.readline


def dfs(city, cnt, value, first_v):
    global min_v

    if cnt == n:
        if arr[city][first_v]:
            min_v = min(min_v, value + arr[city][first_v])
        return
    if min_v < value:
        return
    for i in range(n):
        if not visited[i] and arr[city][i]:
            visited[i] = 1
            dfs(i, cnt + 1, value + arr[city][i], first_v)
            visited[i] = 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


min_v = int(1e9)
visited = [0] * n
for idx in range(n):
    visited[idx] = 1
    dfs(idx, 1, 0, idx)
    visited[idx] = 0
print(min_v)