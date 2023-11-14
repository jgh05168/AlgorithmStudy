import sys
from collections import deque

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
hd = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
      (1, -2), (2, -1), (2, 1), (1, 2)]

def check(nr, nc, k): # 이동 가능 여부 확인
    if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc][k] and maps[nr][nc] == 0:
        return True
    return False

def bfs():
    queue = deque([(0, 0, 0)])
    while queue:
        r, c, k = queue.popleft()
        if r == H-1 and c == W-1: # 도착점인 경우
            return visited[r][c][k]-1 # 동작수의 최소값 return
        for idx in range(4): # 4방향으로 이동하는 경우
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if check(nr, nc, k):
                queue.append((nr, nc, k))
                visited[nr][nc][k] = visited[r][c][k] + 1
        if k < K: # '말'의 움직임으로 이동하는 경우(k사용)
            for idx in range(8):
                nr = r + hd[idx][0]
                nc = c + hd[idx][1]
                if check(nr, nc, k+1):
                    queue.append((nr, nc, k+1))
                    visited[nr][nc][k+1] = visited[r][c][k] + 1
    return -1 # 도착점으로 이동하지 못할 경우 -1 return

K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1

print(bfs())