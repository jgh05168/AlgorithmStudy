'''
배열 돌리ㅐ기

그냥 배열 돌려보면서 각 행의 합 중 최솟값 찾기
시계방향으로 한 칸씩 돌린다.
(r, c, s) => 윗 칸 : (r - s, c - s), 아랫칸 : (r + s, c + s)]

연산 개수 : k번 < 6
    - 조합 사용(selected)
'''

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def rotate(order, arr):
    start, end, s = order
    tmp_arr = [[0] * m for _ in range(n)]
    sr, sc, er, ec = start - 1 - s, end - 1 - s, start + s, end + s
    depth = 1
    tmp_arr[start - 1][end - 1] = arr[start - 1][end - 1]
    while (sr, sc) != (start - 1, end - 1):
        d = 0
        r, c = sr, sc
        while True:
            nr, nc = r + dr[d], c + dc[d]
            if not (sr <= nr < er and sc <= nc < ec):
                d = (d + 1) % 4
                continue
            tmp_arr[nr][nc] = arr[r][c]
            if (nr, nc) == (sr, sc):
                break
            r, c = nr, nc
        sr, sc, er, ec = sr + depth, sc + depth, er - depth, ec - depth

    for i in range(n):
        for j in range(m):
            if not tmp_arr[i][j]:
                tmp_arr[i][j] = arr[i][j]

    return tmp_arr


def dfs(cnt, arr):
    global ans
    if cnt == k:
        for i in range(n):
            ans = min(ans, sum(arr[i]))
    else:
        for i in range(k):
            if not selected[i]:
                selected[i] = 1
                dfs(cnt + 1, rotate(order[i], arr))
                selected[i] = 0


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
order = []
for _ in range(k):
    order.append(tuple(map(int, input().split())))
selected = [0] * k

ans = int(1e9)

dfs(0, arr)

print(ans)