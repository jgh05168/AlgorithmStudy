from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def gravity(grid):
    for j in range(w):
        stack = []
        for i in range(h):
            if grid[i][j]:
                stack.append(grid[i][j])
        for i in range(h-1, -1, -1):
            if stack:
                grid[i][j] = stack.pop()
            else:
                grid[i][j] = 0
    return grid

def burst(grid, r, c):
    queue = deque([(r, c, grid[r][c])])
    visited = [[False] * w for _ in range(h)]
    visited[r][c] = True
    removed = [(r, c)]
    grid[r][c] = 0

    while queue:
        r, c, power = queue.popleft()
        for d in range(4):
            nr, nc = r, c
            for _ in range(power - 1):
                nr += dr[d]
                nc += dc[d]
                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc]:
                    queue.append((nr, nc, grid[nr][nc]))
                    visited[nr][nc] = True
                    removed.append((nr, nc))
                    grid[nr][nc] = 0
    return removed

def dfs(grid, depth, removed_count):
    global max_removed
    if depth == n or removed_count == total:
        max_removed = max(max_removed, removed_count)
        return

    for j in range(w):
        for i in range(h):
            if grid[i][j]:
                original_grid = [row[:] for row in grid]
                removed = burst(grid, i, j)
                gravity(grid)
                dfs(grid, depth + 1, removed_count + len(removed))
                grid = original_grid
                break

t = int(input())
for tc in range(1, t + 1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    total = sum(1 for i in range(h) for j in range(w) if board[i][j])

    # 게임 시작
    max_removed = 0
    dfs(board, 0, 0)

    print(f'#{tc} {total - max_removed}')
