from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(scrash, srow, scol):
    queue = deque([(scrash, srow, scol)])
    visited[0][0][0] = 1

    while queue:
        crash, row, col = queue.popleft()
        # 도착지인 경우
        if (row, col) == (N - 1, M - 1):
            return visited[crash][row][col]
        else:
            for d in range(len(dr)):
                nrow = row + dr[d]
                ncol = col + dc[d]
                if 0 <= nrow < N and 0 <= ncol < M:
                    # 만약 crash == 1 인 경우, visited[crash][nrow][ncol]를 방문했다면,
                    # 굳이 queue에 업데이트 해 줄 필요가 없다 -> 최소 경로를 찾아야 하기 때문

                    # 벽이 아닌 경우, 방문하지 않은 경우
                    if not grid[nrow][ncol] and not visited[crash][nrow][ncol]:
                        visited[crash][nrow][ncol] = visited[crash][row][col] + 1
                        queue.append((crash, nrow, ncol))
                    # 벽을 만난 경우, 벽을 부수지 않은 경우
                    if grid[nrow][ncol] and not crash:
                        visited[crash + 1][nrow][ncol] = visited[crash][row][col] + 1
                        queue.append((crash + 1, nrow, ncol))
    return -1

N, M = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(N)]
# visited[0] : 벽을 부수지 않고 이동하는 경우
# visited[1] : 벽을 한 칸 부순 뒤 이동하는 경우
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

print(bfs(0, 0, 0))