import sys
sys.setrecursionlimit(10**6)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(row, col):
    global cnt
    for d in range(len(dr)):
        nrow, ncol = row + dr[d], col + dc[d]
        if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] == 0 and (nrow, ncol) in trashes:
            cnt += 1
            visited[nrow][ncol] = 1
            dfs(nrow, ncol)


N, M, K = map(int, input().split())
visited = [[-1] * M for _ in range(N)]

trashes = []

for _ in range(K):
    v, w = map(int, input().split())
    trashes.append((v - 1, w - 1))
    visited[v - 1][w - 1] = 0

cnt = 0
max_cnt = 0
for row, col in trashes:
    if not visited[row][col]:
        cnt = 0
        dfs(row, col)
        if max_cnt < cnt:
            max_cnt = cnt

print(max_cnt)