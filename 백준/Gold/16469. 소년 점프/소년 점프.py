'''
visited 3 개 만들기
각 구간 모두 값이 존재한다면 겹치는 값 중 최대값이 모인 시간의 최소값임.
    이 안에 조건문 걸어주어 만약 모인 값보다 현재 값이 더 적다면 지점 개수 1로 초기화, 같다면 1 더해주기
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(badguys):
    global min_merge, merge_cnt, is_valid
    queue = badguys

    while queue:
        row, col, person = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and visited[person][nrow][ncol] == -1 and not maze[nrow][ncol]:
                visited[person][nrow][ncol] = visited[person][row][col] + 1
                queue.append((nrow, ncol, person))

    for i in range(n):
        for j in range(m):
            if visited[0][i][j] >= 0 and visited[1][i][j] >= 0 and visited[2][i][j] >= 0:
                if max(visited[0][i][j], visited[1][i][j], visited[2][i][j]) < min_merge:
                    min_merge = max(visited[0][i][j], visited[1][i][j], visited[2][i][j])
                    merge_cnt = 1
                elif max(visited[0][i][j], visited[1][i][j], visited[2][i][j]) == min_merge:
                    merge_cnt += 1
                is_valid = True


n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
bad_gyus = deque()
visited = [[[-1] * m for _ in range(n)] for _ in range(3)]
for i in range(3):
    r, c = map(int, input().split())
    bad_gyus.append((r - 1, c - 1, i))
    visited[i][r - 1][c - 1] = 0
min_merge = int(1e9)
merge_cnt = 0
is_valid = False

bfs(bad_gyus)

if is_valid:
    print(min_merge)
    print(merge_cnt)
else:
    print(-1)