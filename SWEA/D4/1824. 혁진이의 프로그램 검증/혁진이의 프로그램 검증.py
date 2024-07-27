'''
현재 위치에 있는 문자가 나타내는 명령을 처리하고, 이동 방향에 따라 다음 문자로 이동해야 함
    - 가장 처음 위치는 제일 왼쪽 위에 있는 문자이고, 이동 방향은 오른쪽
이동 방향이 상하좌우로 바뀔 수 있다.
    - 다음 이동이 격자를 벗어나면, 반대편 위치로 이동한다.
    - 메모리가 단 하나. 0 ~ 15 정수 저장

풀이:
단순 구현
- 여러 번 방문해도 된다.
    - 숫자별로 visited 배열을 3차원으로 생성한다.
    - 이미 가 본 부분이라면 continue
- dict 사용하여 문자에 대해 조건 처리
- @ 을 만날 때까지 진행
    - 못만나고 끝나면 NO 출력
'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

dir_dict = {'>' : 0, 'v': 1, '<': 2, '^': 3}

def dfs(r, c, memory, d):
    global ans



t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]

    sr, sc, memory, sd = 0, 0, 0, 0
    visited = [[[[0] * m for _ in range(n)] for _ in range(16)] for _ in range(4)]

    ans = False

    stack = [(sr, sc, memory, sd)]

    while stack:
        r, c, memory, d = stack.pop()
        order = grid[r][c]

        # 종료 조건
        if order == '@':
            ans = True
            break
        if visited[d][memory][r][c]:
            continue
        else:
            # 이어가는 조건
            visited[d][memory][r][c] = 1
            nd, nmemory = d, memory

            if order in dir_dict.keys():
                nd = dir_dict[order]
            elif order == '_':
                if not memory:
                    nd = 0
                else:
                    nd = 2
            elif order == '|':
                if not memory:
                    nd = 1
                else:
                    nd = 3
            elif '0' <= order <= '9':
                nmemory = int(order)
            elif order == '+':
                nmemory = (memory + 1) % 16
            elif order == '-':
                nmemory = (memory - 1) % 16

            if order == '?':
                for tmp_d in range(4):
                    tmp_nr, tmp_nc = (r + dr[tmp_d]) % n, (c + dc[tmp_d]) % m
                    if visited[tmp_d][memory][tmp_nr][tmp_nc]:
                        continue
                    stack.append((tmp_nr, tmp_nc, nmemory, tmp_d))
            else:
                nr, nc = (r + dr[nd]) % n, (c + dc[nd]) % m
                stack.append((nr, nc, nmemory, nd))

    if not ans:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')

