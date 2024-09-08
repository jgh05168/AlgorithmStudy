'''
배열 회전 후 최솟값 리턴
'''
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotate(sx, sy, ex, ey):
    d = 0
    x, y = sx + dx[d], sy + dy[d]
    cur_val = grid[x][y]
    grid[x][y] = grid[sx][sy]
    min_v = grid[x][y]
    while (x, y) != (sx, sy):
        nx, ny = x + dx[d], y + dy[d]
        # 범위를 벗어난 경우
        if not (sx <= nx < ex and sy <= ny < ey):
            nx, ny = x + dx[(d + 1) % 4], y + dy[(d + 1) % 4]
            d = (d + 1) % 4
        # 값 옮겨주기
        bef_val = grid[nx][ny]
        grid[nx][ny] = cur_val
        cur_val = bef_val
        min_v = min(min_v, grid[nx][ny])

        # 값 업데이트
        x, y = nx, ny

    return min_v

def solution(rows, columns, queries):
    answer = []
    num = 1
    for i in range(rows):
        tmp = []
        for j in range(columns):
            tmp.append(num)
            num += 1
        grid.append(tmp)

    for i in range(len(queries)):
        sr, sc, er, ec = queries[i]
        answer.append(rotate(sr - 1, sc - 1, er, ec))
    return answer

grid = []