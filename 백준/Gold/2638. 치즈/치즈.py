'''
전략

1. bfs로 바깥부분을 탐색하며 바깥부분과 치즈 겉면을 체크

1.5. 치즈 겉면을 체크하며 없어질 바깥 치즈 정보 체크

2. 없어질 치즈 바깥 부분부터 탐색
    2-1. 네 방면에 대해 조사를 진행
    2-2. 만약 공기를 만난다면 bfs 진행하여 빈 부분을 바깥 공기값으로 변경

3. 2 반복
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 바깥 부분을 체크하기 위한 초기 bfs
def find_outer_bfs(srow, scol):
    queue = deque([(srow, scol)])
    visited[srow][scol] = -1

    while queue:
        row, col = queue.popleft()
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not visited[nrow][ncol] and not grid[nrow][ncol]:
                visited[nrow][ncol] = -1
                queue.append((nrow, ncol))


# 바깥 치즈를 체크하기 위한 bfs
def find_outer_cheese(cheeses):
    outer_cheese = deque()

    while cheeses:
        row, col = cheeses.popleft()
        visited[row][col] = 1
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] < 1:
                if visited[nrow][ncol] == -1:
                    visited[row][col] += 1
        if visited[row][col] > 2:
            outer_cheese.append((row, col))
        else:
            visited[row][col] = 1

    return outer_cheese


def change_area(outer_cheeses):
    while outer_cheeses:
        row, col = outer_cheeses.popleft()
        visited[row][col] = -1
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not visited[nrow][ncol]:
                find_outer_bfs(nrow, ncol)


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cheeses = deque()

# 가장 가까운 첫번째 바깥영역 좌표 찾기 & 치즈부분 찾기
first_out = False
for i in range(N):
    for j in range(M):
        if not grid[i][j] and not first_out:
            sout_idx = (i, j)
            first_out = True
            break
        elif grid[i][j]:
            cheeses.append((i, j))


find_outer_bfs(sout_idx[0], sout_idx[1])


cnt = 0
while cheeses:
    # 치즈 바깥쪽부터 체크
    # visited = -1 : 바깥쪽
    # visited = 0 : 방문을 안해봄
    # visited = 1 : 방문은 함
    # visited = 2 ~ 5 : 바깥에 닿는 면이 몇 갠지
    set_cheeses = set(cheeses)
    outer_cheeses = find_outer_cheese(cheeses)

    cheeses = deque(set(set_cheeses).difference(set(outer_cheeses)))
    # 공간이 뚫린다면 바깥 영역으로 바꿔주는 역할
    change_area(outer_cheeses)

    cnt += 1

print(cnt)
