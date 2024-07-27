'''
rxc
지뢰가 없는 칸이라면, 주위 8칸에 대해 몇 개의 지뢰가 있는지 클릭한 칸에 표시
    - 숫자가 0이라면, 그 8방향 칸도 자동으로 숫자를 표시해준다. (8방향의 각각에 대해서도 조사) - bfs
어떤 위치에 지뢰가 있는지 알고있음

최소 횟수를 출력
풀이:
bfs로 진행
1. 0인 지점을 먼저 찾고, 거기서부터 bfs 돌리기
2. visited를 global로 설정하여 방문 안 한 부분이라면 추가적으로 터트려주기
'''

from collections import deque

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def bfs(sr, sc):
    queue = deque([(sr, sc)])
    visited[sr][sc] = 1

    while queue:
        r, c = queue.popleft()
        visited[r][c] = 1

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if not grid[nr][nc]:
                    queue.append((nr, nc))
                visited[nr][nc] = 1


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    grid = [list(input()) for _ in range(n)]

    visited = [[0] * n for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == '.':
                tmp = 0
                for k in range(8):
                    ni, nj = i + dr[k], j + dc[k]
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == '*':
                            tmp += 1
                grid[i][j] = tmp

    # 주변 하나도 없는 애들에 대해 bfs 진행
    for i in range(n):
        for j in range(n):
            if not grid[i][j] and not visited[i][j]:
                bfs(i, j)
                ans += 1

    # 남은 잔존세력들 처리하기
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] != '*':
                visited[i][j] = 1
                ans += 1

    print(f'#{tc} {ans}')