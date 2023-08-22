import sys
sys.setrecursionlimit(10**6)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(row, col, code):
    if visited[row][col]:
        return
    else:
        global width
        width += 1
        visited[row][col] = True
        for d in range(len(dr)):
            nrow = row + dr[d]
            ncol = col + dc[d]
            if 0 <= nrow < H and 0 <= ncol < W and not visited[nrow][ncol] and paper[nrow][ncol] == code:
                dfs(nrow, ncol, code)

W, H = map(int, input().split())
N = int(input())

paper = [[0] * W for _ in range(H)]

check = 1
for _ in range(N):
    way, idx = map(int, input().split())
    if not way:
        for row in range(idx):
            for col in range(W):
                paper[row][col] += check
    else:
        for row in range(H):
            for col in range(idx):
                paper[row][col] += check
    check += 1

max_width = 0
visited = [[False] * W for _ in range(H)]
for row in range(H):
    for col in range(W):
        width = 0
        if not visited[row][col]:
            code = paper[row][col]
            dfs(row, col, code)
            if max_width < width:
                max_width = width

print(max_width)
