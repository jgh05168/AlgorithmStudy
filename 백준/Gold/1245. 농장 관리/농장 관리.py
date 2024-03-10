'''
산봉우리마다 경비원 배치 -> 농장에 산봉우리가 몇 개인지 구하기

산봉우리 :
- 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합
- 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야 함

풀이 :
1. 이중 for문 돌면서 방문 않 한 곳이라면 bfs
    - 만약 탐색 중 자신보다 큰 봉우리가 존재한다면 flag = 1 설정 후 이어서 탐색
    - 값이 같은 부분만 queue에 저장
2. 모든 봉우리를 탐색하고 종료한다면, cnt+=1
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def bfs(srow, scol):
    queue = deque([(srow, scol)])
    visited[srow][scol] = 1
    top = grid[srow][scol]
    flag = 1
    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m:
                if grid[nrow][ncol] > grid[row][col]:
                    flag = 0
                elif not visited[nrow][ncol] and grid[nrow][ncol] == grid[row][col]:
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = 1

    if flag:
        return 1


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
# 1. 봉우리 탐색
tops = []
for i in range(n):
    for j in range(m):
        if grid[i][j] and not visited[i][j]:
            if bfs(i, j):
                cnt += 1

print(cnt)