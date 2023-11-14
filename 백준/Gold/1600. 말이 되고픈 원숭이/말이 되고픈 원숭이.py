'''
말처럼 움직이는 경우 & 한 번씩 움직이는 경우에 대해서 따로 설정하여 deque에 저장

 -> 조건 설정이 필요
    1. k번 이하 만큼 움직였는가?
    2. 갈 수 있는 위치인가?

 - k의 범위 : 0 <= k <= 30
    -> visited 배열을 3차원으로 생성 & k개만큼 생성해도 가능하다.

deque에 (row, col, 말처럼 이동한 경우) 정보 저장
오른쪽 아래 도착하면 바로 return
'''


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
