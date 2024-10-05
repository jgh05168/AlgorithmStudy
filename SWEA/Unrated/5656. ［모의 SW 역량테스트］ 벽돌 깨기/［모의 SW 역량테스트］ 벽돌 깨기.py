'''
20:32

구슬을 쏘아 벽돌을 깨자
n번 구슬 쏘기
1. 구슬은 열로만 움직일 수 있고, 항상 맨 위의 벽돌만 깨뜨린다
2. 벽돌은 숫자 1 ~ 9로 표현되며, 구슬이 명중한 벽돌은 상화좌우 숫자 - 1만큼 같이 제거된다.
3. 제거되는 벽돌은 동시에 제거된다.
4. 중력 작용

풀이:
queue에 구슬맞은 벽돌 넣은 뒤 밤위만큼 없애주기
    - 만약 반응하는 벽돌을 만나면, queue에 삽입
    - 이후, 같이 부숴주기

'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def gravity(grid):
    new_grid = [row[:] for row in grid]
    for i in range(h - 1, -1, -1):
        for j in range(w):
            if new_grid[i][j]:
                ni = i + 1
                while ni < h and not new_grid[ni][j]:
                    ni += 1
                ni -= 1
                if i != ni:
                    new_grid[ni][j] = new_grid[i][j]
                    new_grid[i][j] = 0

    return new_grid

def dfs(grid, depth, pung):
    global ans, max_pung
    if depth == n:
        if pung > max_pung:
            ans = total - pung
            max_pung = pung
        return
    for j in range(w):
        tmp = []
        for i in range(h):
            if grid[i][j]:
                pung_list = deque([(i, j)])
                power_list = deque([grid[i][j]])
                tmp.append((i, j, grid[i][j]))
                grid[i][j] = 0

                # 폭탙 터뜨려보기
                if tmp[0][2] > 1:
                    while pung_list:
                        r, c = pung_list.popleft()
                        power = power_list.popleft()

                        for d in range(len(dr)):
                            nr, nc = r + dr[d], c + dc[d]
                            tmp_power = power - 1

                            while 0 <= nr < h and 0 <= nc < w and tmp_power:
                                if grid[nr][nc]:
                                    if grid[nr][nc] > 1:
                                        pung_list.append((nr, nc))
                                        power_list.append(grid[nr][nc])
                                    tmp.append((nr, nc, grid[nr][nc]))
                                    grid[nr][nc] = 0
                                nr += dr[d]
                                nc += dc[d]
                                tmp_power -= 1
                break
        # 중력 작용
        new_grid = gravity(grid)
        dfs(new_grid, depth + 1, pung + len(tmp))
        while tmp:
            r, c, val = tmp.pop()
            grid[r][c] = val


t = int(input())
for tc in range(1, t + 1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    total = 0
    for i in range(h):
        for j in range(w):
            if board[i][j]:
                total += 1

    # 게임 시작
    max_pung = 0
    ans = 0
    dfs(board, 0, 0)        # depth, value

    print(f'#{tc} {ans}')