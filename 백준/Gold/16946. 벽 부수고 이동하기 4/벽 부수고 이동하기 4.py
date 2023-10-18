'''
벽뿌수고 이동하기 4

1. 빈칸인 부분이 각각 몇 개인지 bfs를 통해 확인. 이후 각 빈칸 별 빈 칸 개수를 딕셔너리로 저장
2. 벽인 부분에 대해 인접 4방향으로 탐색. 만약 빈칸이라면 딕셔너리에서 해당 빈칸의 개수를 가져와 더해준다.
3. 맵 업데이트

-------- 시간초과 ---------
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol, color):
    queue = deque()
    queue.append((srow, scol))
    visited_zeros[srow][scol] = color

    cnt = 1
    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not visited_zeros[nrow][ncol] and grid[nrow][ncol] == '0':
                visited_zeros[nrow][ncol] = color
                queue.append((nrow, ncol))
                cnt += 1

    zeros_dict.update({color: cnt})


N, M = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]
visited_zeros = [[0] * M for _ in range(N)]

zeros_dict = {}
walls = []
color = 1
for i in range(N):
    for j in range(M):
        if grid[i][j] == '0' and not visited_zeros[i][j]:       # 빈칸이고, 방문한 적 없다면 bfs 탐색
            bfs(i, j, color)
            color += 1
        elif grid[i][j] == '1':
            walls.append((i, j))

# 벽인 부분에 대해 4방면 탐색 후 값 저장해서 넘기기
ans = [['0'] * M for _ in range(N)]
for wrow, wcol in walls:
    check_area = set()
    temp_ans = 1
    for d in range(len(dr)):
        nrow, ncol = wrow + dr[d], wcol + dc[d]
        if 0 <= nrow < N and 0 <= ncol < M and grid[nrow][ncol] == '0' and visited_zeros[nrow][ncol]:
            check_area.add(visited_zeros[nrow][ncol])
    for add_val in check_area:
        temp_ans += zeros_dict[add_val]

    ans[wrow][wcol] = str((temp_ans % 10))

for i in range(N):
    print(''.join(ans[i]))