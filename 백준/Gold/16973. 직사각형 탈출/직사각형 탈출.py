dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 시간초과 방지를 위한 수정 코드
# 2중 반복문으로 한 칸씩 check하여 벽의 위치인지 확인하는 방법을 사용하면 시간초과 발생
# 따라서 미리 벽의 위치를 저장해둔 뒤, 현재 row ~ row + H, col ~ col + W 사이에 벽의 좌표가 존재한다면, 갈 수 없는 것으로 체크
def checking(nrow, ncol):
    for rwall, cwall in walls:
        if nrow <= rwall < nrow + H and ncol <= cwall < ncol + W:
            return False
    return True

def bfs(srow, scol):
    queue = []
    visited = [[0] * M for _ in range(N)]
    queue.append((srow, scol))
    visited[srow][scol] = 1

    while queue:
        row, col = queue.pop(0)
        for d in range(len(dr)):
            nrow = row + dr[d]
            ncol = col + dc[d]
            # 아래 조건문을 만족하는지 확인 후 이동
            if 0 <= nrow < N and 0 <= ncol < M and 0 <= nrow + H - 1 < N and 0 <= ncol + W - 1 < M and visited[nrow][ncol] == 0:
                if checking(nrow, ncol):    # 이동이 가능한지 확인
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] += visited[row][col] + 1
                    if nrow == Fr - 1 and ncol == Fc - 1:
                        return visited[nrow][ncol] - 1

    return -1


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

# 이중 for문을 사용하여 벽의 좌표를 미리 저장
walls = []
for row in range(N):
    for col in range(M):
        if grid[row][col] == 1:
            walls.append((row, col))

print(bfs(Sr - 1, Sc - 1))