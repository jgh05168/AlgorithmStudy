'''
생명력
    - 초기 상태에서 줄기 세포들은 비활성 상태
    - 생명력 x인 세포는 x시간 동안 비활성 상태
        - x시간이 지나는 순간 활성 상태가 된다.
    - 활성 상태
        - x시간동안 살아있을 수 있으며, 이후 죽는다.
        - 죽은 상태로 해당 grid를 차지한다.
        - 활성 + 1 시간동안 4방향으로 번식
            - 번식된 세포는 비활성
            - 생명력 수치가 높은 애가 번식한다.
k 시간 후 살아있는 줄기세포의 개수를 구하라

풀이:
활성 queue, 활성 + 1 queue 사용
map 크기 : grid[n + k + 1][n + k + 1]
'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    input_grid = [list(map(int, input().split())) for _ in range(n)]
    grid = [[0] * 500 for _ in range(500)]
    deactivate_cells = deque()
    activate_cells = []
    for i in range(n):
        for j in range(m):
            grid[500 // 2 - (n // 2) + i + 1][500 // 2 - (m // 2) + j + 1] = input_grid[i][j]
            if input_grid[i][j]:
                deactivate_cells.append((500 // 2 - (n // 2) + i + 1, 500 // 2 - (m // 2) + j + 1, input_grid[i][j]))

    for _ in range(k):
        new_activate = deque()
        new_deactivate = []

        # 1. activate로 넘어갈 수 있는지 확인
        tmp_deactivate = deque()
        while deactivate_cells:
            r, c, life = deactivate_cells.popleft()
            life -= 1
            if life:
                tmp_deactivate.append((r, c, life))
            else:
                new_activate.append((r, c, grid[r][c], grid[r][c]))     # 행, 열, 현재 생명력, 초기 생명력
        deactivate_cells.extend(tmp_deactivate)

        # 2. activate 체크
        if activate_cells:
            activate_cells.sort(key=lambda x: x[3])
        while activate_cells:
            r, c, cur_life, s_life = activate_cells.pop()
            cur_life -= 1
            # 셀 죽었는지 체크
            if cur_life == 0:
                grid[r][c] = -1
            else:
                new_activate.append((r, c, cur_life, s_life))
            # 번식 가능한지 체크
            if cur_life + 1 == s_life:
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = s_life
                        new_deactivate.append((nr, nc, s_life))

        # 초기화
        deactivate_cells.extend(new_deactivate)
        activate_cells.extend(new_activate)

    ans = len(deactivate_cells) + len(activate_cells)
    print(f'#{tc} {ans}')