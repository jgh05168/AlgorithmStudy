'''
빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어든다
동서남북 네 방향으로 붙어있는 0 이 저장된 칸의 개수만큼

1. 빙산의 개수를 count
2. 4방향 탐색 진행 -> 처음부터 줄이지 말고 스택에 값, 위치를 저장
3. 빙산 크기 줄이기
4. 빙산들에 대해서 bfs 진행 -> 빙산이 분리되었다면 break
300 * 300 * 300
'''


from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol))
    visited[srow][scol] = 1

    while queue:
        row, col = queue.popleft()
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not visited[nrow][ncol] and grid[nrow][ncol]:
                visited[nrow][ncol] = 1
                queue.append((nrow, ncol))


N, M = map(int, input().split())    # 행, 열
grid = [list(map(int, input().split())) for _ in range(N)]

icebergs = deque()
# 초기 빙산의 위치를 저장
for i in range(N):
    for j in range(M):
        if grid[i][j]:
            icebergs.append((i, j))

year = 0
# 빙산이 분리되면 break
while True:
    visited = [[0] * M for _ in range(N)]
    temp_list = deque()

    # 만약 다 녹았는데도 분리되지 않는다면, 0을 출력
    if not icebergs:
        year = 0
        break

    while icebergs:
        row, col = icebergs.popleft()
        height = grid[row][col]

        # 4방면 탐색
        melting = 0
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and not grid[nrow][ncol]:
                melting += 1

        new_height = height - melting
        if new_height < 0:    # 만약 빙산의 높이가 0보다 낮다면, 0으로 값 설정
            new_height = 0

        temp_list.append((row, col, new_height))

    # 연차 업데이트
    year += 1

    # 위치정보 업데이트
    while temp_list:
        row, col, new_height = temp_list.popleft()
        if new_height:      # 아직 얼음이 덜녹았으면, 다시 큐에 위치 저장
            icebergs.append((row, col))
        grid[row][col] = new_height

    # 덩이가 나뉘어졌는지 확인
    iceberg_cnt = 0
    check = False
    for row, col in icebergs:
        if not visited[row][col]:
            bfs(row, col)
            iceberg_cnt += 1
        if iceberg_cnt > 1:     # 덩이로 나뉘어졌다면 종료
            check = True
            break

    # 만약 덩이가 갈라졌다면
    if check:
        break

print(year)