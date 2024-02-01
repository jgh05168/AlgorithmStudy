from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

endpoint = (0, 0)
min_move = int(1e9)
n, m = 0, 0


def bfs(board, n, m, srow, scol):
    global min_move
    queue = deque()
    queue.append((srow, scol, 0))       # row, col, move_cnt
    visited = [[[0] * m for _ in range(n)] for _ in range(4)]       # 현재 위치에 온 적이 있는지만 체크

    while queue:
        row, col, move_cnt = queue.popleft()
        if move_cnt >= min_move:
            continue
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[d][row][col] and board[nrow][ncol] != 'D':
                visited[d][row][col] = 1
                crow, ccol = nrow + dr[d], ncol + dc[d]
                while 0 <= crow < n and 0 <= ccol < m and board[crow][ccol] != 'D':
                    nrow, ncol = crow, ccol
                    crow += dr[d]
                    ccol += dc[d]
                if (nrow, ncol) == endpoint:
                    if move_cnt + 1 < min_move:
                        min_move = move_cnt + 1
                else:
                    queue.append((nrow, ncol, move_cnt + 1))
                    
    return
    

def solution(board):
    global n, m, endpoint, min_move
    n, m = len(board), len(board[0])
    srow, scol = 0, 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                srow, scol = i, j
            elif board[i][j] == 'G':
                endpoint = (i, j)
                
    bfs(board, n, m, srow, scol)
    if min_move != int(1e9):
        answer = min_move
    else:
        answer = -1

    return answer