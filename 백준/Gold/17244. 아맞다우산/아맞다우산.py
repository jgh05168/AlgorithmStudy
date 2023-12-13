'''
visited를 비트마스킹으로 설정한다.

비트 정보를 queue에 같이 넣어주어 그것에 대한 visited를 사용
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol, 0, 0))
    visited[0][srow][scol] = 0      # 물건을 찾기 전 초기 위치

    while queue:
        row, col, v_idx, find_stuffs = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and visited[v_idx][nrow][ncol] == -1 and home[nrow][ncol] != '#':
                # 만약 특정 짐들을 모두 찾았고, 도착점에 도착했다면 종료
                if home[nrow][ncol] == 'E' and find_stuffs == stuffs:
                    return visited[v_idx][row][col] + 1
                if home[nrow][ncol].isdigit():
                    # 만약 이전에 이미 챙긴 짐이라면 그냥 이어서 진행하기
                    if v_idx & (1 << int(home[nrow][ncol])):
                        visited[v_idx][nrow][ncol] = visited[v_idx][row][col] + 1
                        queue.append((nrow, ncol, v_idx, find_stuffs))
                    else:       # 아니라면 새로운 visited로 추가
                        visited[v_idx + (1 << int(home[nrow][ncol]))][nrow][ncol] = visited[v_idx][row][col] + 1
                        queue.append((nrow, ncol, v_idx + (1 << int(home[nrow][ncol])), find_stuffs + 1))
                else:
                    visited[v_idx][nrow][ncol] = visited[v_idx][row][col] + 1
                    queue.append((nrow, ncol, v_idx, find_stuffs))
    return 0


m, n = map(int, input().split())
home = [list(input().rstrip()) for _ in range(n)]
stuffs = 0
for i in range(n):
    for j in range(m):
        if home[i][j] == 'S':
            sr, sc = i, j
        elif home[i][j] == 'X':
            home[i][j] = str(stuffs)
            stuffs += 1

visited = [[[-1] * m for _ in range(n)] for i in range(1 << stuffs)]
print(bfs(sr, sc))