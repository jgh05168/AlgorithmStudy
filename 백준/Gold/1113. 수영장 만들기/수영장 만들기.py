'''
1113. 수영장 만들기

풀이:
최대 50 x 50
1. 벽인 부분부터 체크
    - 사이드 돌면서 같은 부분 다 bfs로 묶은 다음 죽이기
2. 물 받을 수 있는 곳 체크
    - 벽이고 나보다 크다면, 물 받기
    - 만약 벽보다 내가 더 크다면 죽기
------------ 왜인지 모르겠지만 실패 -------------
물을 바닥부터 채워주는 방식으로 진행
- 한 칸 씩 계속 세어주는 방식으로 res를 계산한다.
    - ex) 만약 물이 5고 9까지 막혀있으면, +1 +1 +1 +1 하는 방식
'''

import sys
from collections import deque

res = 0

# 수영장이 될 수 있는지 확인하고 되면 물 양 더하기
def bfs(sx, sy, h):
    global res, visited

    que = deque([(sx, sy)])

    flag = True  # 수영장이 될 수 있는지 체크하는 변수

    visited[sx][sy] = True
    cnt = 1
    while que:
        x, y = que.popleft()

        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            # 수영장 밖으로 물이 넘치면 flag False로 하고 연결된 나머지 전부 체크(수영장이 안되는 위치 전부)
            if not (0 <= nx < N and 0 <= ny < M):
                flag = False
                continue

            if board[nx][ny] <= h and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))
                cnt += 1
    if flag:
        res += cnt

N, M = map(int, input().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 수면을 1부터 8까지 올리면서 확인
for num in range(1, 9):
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # 현재 수면보다 낮고 아직 체크 안한 곳
            if board[i][j] <= num and not visited[i][j]:
                bfs(i, j, num)
print(res)


