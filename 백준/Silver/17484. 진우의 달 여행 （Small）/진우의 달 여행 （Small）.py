'''
- 우주선이 움직일 수 있는 방향 : 아래 세가지 경우
- 우주선은 같은 방향으로 두 번 연속 움직일 수 없다.

연료의 최솟값을 구하자

- 최대 길이 : 6이므로 완전탐색을 진행해도 시간이 남는다.
    - 재귀를 사용한 완전탐색 진행
n^2 * 3
'''

import sys
input = sys.stdin.readline

dr = [1, 1, 1]
dc = [-1, 0, 1]

def dfs(row, col, cur_d, val):
    # 종료 조건
    global min_v
    if row == n - 1:
        min_v = min(min_v, val)
        return

    else:
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and d != cur_d:
                dfs(nrow, ncol, d, val + space[nrow][ncol])


n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
min_v = int(1e9)
for i in range(m):
    dfs(0, i, -1, space[0][i])

print(min_v)