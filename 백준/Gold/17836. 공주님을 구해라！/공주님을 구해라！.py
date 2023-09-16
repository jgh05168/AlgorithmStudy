'''
1. bfs로 최단거리 탐색 진행

2. 만약 칼을 먹었다면 벽 상관 없이 바로 공주한테 가기

3. 도착한 시간과 T를 비교
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol))
    after_queue = deque()
    can_go = True
    get_gram = True
    while queue:
        row, col = queue.popleft()
        if (row, col) == (N - 1, M - 1):
            break

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not visited[nrow][ncol] and castle[nrow][ncol] != 1:
                if castle[nrow][ncol] == 2:
                    after_visited[nrow][ncol] = visited[row][col] + 1
                    after_queue.append((nrow, ncol))
                visited[nrow][ncol] = visited[row][col] + 1
                queue.append((nrow, ncol))

    if not visited[N - 1][M - 1]:
        can_go = False

    while after_queue:
        row, col = after_queue.popleft()
        if (row, col) == (N - 1, M - 1):
            break

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not after_visited[nrow][ncol]:
                    after_visited[nrow][ncol] = after_visited[row][col] + 1
                    after_queue.append((nrow, ncol))

    if not after_visited[N - 1][M - 1]:
        get_gram = False


    if not can_go and not get_gram:
        return T + 1
    elif not can_go and get_gram:
        return after_visited[N - 1][M - 1]
    elif not get_gram and can_go:
        return visited[N - 1][M - 1]
    else:
        return min(visited[N - 1][M - 1], after_visited[N - 1][M - 1])


N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
after_visited = [[0] * M for _ in range(N)]
escape_time = bfs(0, 0)

if T < escape_time:
    print('Fail')
else:
    print(escape_time)