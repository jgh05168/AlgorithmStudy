'''
- 현재 위치에 도착하면 갈 수 있는지 여부를 체크
- 현재 위치에서 출발 시 죽는지 안죽는지 여부를 체크할 수 있는 3차원 배열이 필요
    - 만약 죽게된다면 현재까지 이동한 결과값을 저장한다.
- 4방향에 대해 가지치기가 필요함
- 직접 가보는 것이 아닌 방향별로 거리를 빼본다.

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def get_nrow_ncol(row, col, d, move_cnt):
    if d == 0:
        return row, col + move_cnt
    elif d == 1:
        return row + move_cnt, col
    elif d == 2:
        return row, col - move_cnt
    else:
        return row - move_cnt, col


def dfs(row, col, cnt):
    global max_move, inf
    max_move = max(max_move, cnt)
    move_cnt = int(board[row][col])
    for d in range(len(dr)):
        nrow, ncol = get_nrow_ncol(row, col, d, move_cnt)
        # 종료 조건
        if not (0 <= nrow < n and 0 <= ncol < m) or board[nrow][ncol] == 'H':
            continue
        if deadzone[nrow][ncol] < cnt + 1:
            # 무한루프에 빠질 경우
            if visited[nrow][ncol]:
                inf = True
                return

            visited[nrow][ncol] = 1
            deadzone[nrow][ncol] = max(cnt + 1, deadzone[nrow][ncol])
            dfs(nrow, ncol, cnt + 1)
            visited[nrow][ncol] = 0
            if inf:
                return


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
deadzone = [[-1] * m for _ in range(n)]
max_move = 1
inf = False

deadzone[0][0] = 1
dfs(0, 0, 1)

if inf:
    print(-1)
else:
    print(max_move)

