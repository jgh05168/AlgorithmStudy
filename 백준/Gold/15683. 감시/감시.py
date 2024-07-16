'''
5가지 감시 방법이 있음

n = 8이기 떄문에, 완탐돌려도 될 듯

회전은 90도 방향으로 해야 한다.

사각 지대의 최소 크기를 구하자.

재귀 + 시뮬

'''

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def check_room(cnt):
    global ans

    if cnt == cctvs:
        tmp_ans = 0
        for i in range(n):
            for j in range(m):
                if office[i][j] != 6 and not visited[i][j]:
                    tmp_ans += 1
        ans = min(ans, tmp_ans)
        return

    else:
        d_info, row, col = check_idx[cnt]

        if d_info == 1:
            for d in range(len(dr)):
                tmp_loc = set()
                nrow, ncol = row, col
                while 0 <= nrow < n and 0 <= ncol < m and office[nrow][ncol] != 6:
                    if not visited[nrow][ncol]:
                        tmp_loc.add((nrow, ncol))
                    nrow, ncol = nrow + dr[d], ncol + dc[d]
                for nrow, ncol in tmp_loc:
                    visited[nrow][ncol] = 1
                check_room(cnt + 1)
                for nrow, ncol in tmp_loc:
                    visited[nrow][ncol] = 0

        elif d_info == 2:
            for d in range(2):
                tmp_loc = set()
                nrow, ncol = row, col
                brow, bcol = row, col
                while 0 <= nrow < n and 0 <= ncol < m and office[nrow][ncol] != 6:
                    if not visited[nrow][ncol]:
                        tmp_loc.add((nrow, ncol))
                    nrow, ncol = nrow + dr[d], ncol + dc[d]
                while 0 <= brow < n and 0 <= bcol < m and office[brow][bcol] != 6:
                    if not visited[brow][bcol]:
                        tmp_loc.add((brow, bcol))
                    brow, bcol = brow + dr[(d + 2) % 4], bcol + dc[(d + 2) % 4]
                for nrow, ncol in tmp_loc:
                    visited[nrow][ncol] = 1
                check_room(cnt + 1)
                for nrow, ncol in tmp_loc:
                    visited[nrow][ncol] = 0

        elif d_info == 3:
            for d in range(len(dr)):
                tmp_loc = set()
                nrow, ncol = row, col
                brow, bcol = row, col
                while 0 <= nrow < n and 0 <= ncol < m and office[nrow][ncol] != 6:
                    if not visited[nrow][ncol]:
                        tmp_loc.add((nrow, ncol))
                    nrow, ncol = nrow + dr[d], ncol + dc[d]
                while 0 <= brow < n and 0 <= bcol < m and office[brow][bcol] != 6:
                    if not visited[brow][bcol]:
                        tmp_loc.add((brow, bcol))
                    brow, bcol = brow + dr[(d + 3) % 4], bcol + dc[(d + 3) % 4]
                for nrow, ncol in tmp_loc:
                    visited[nrow][ncol] = 1
                check_room(cnt + 1)
                for nrow, ncol in tmp_loc:
                    visited[nrow][ncol] = 0

        elif d_info == 4:
            for d in range(len(dr)):
                tmp_loc = set()
                nrow, ncol = row, col
                brow, bcol = row, col
                trow, tcol = row, col
                while 0 <= nrow < n and 0 <= ncol < m and office[nrow][ncol] != 6:
                    if not visited[nrow][ncol]:
                        tmp_loc.add((nrow, ncol))
                    nrow, ncol = nrow + dr[d], ncol + dc[d]
                while 0 <= brow < n and 0 <= bcol < m and office[brow][bcol] != 6:
                    if not visited[brow][bcol]:
                        tmp_loc.add((brow, bcol))
                    brow, bcol = brow + dr[(d + 3) % 4], bcol + dc[(d + 3) % 4]
                while 0 <= trow < n and 0 <= tcol < m and office[trow][tcol] != 6:
                    if not visited[trow][tcol]:
                        tmp_loc.add((trow, tcol))
                    trow, tcol = trow + dr[(d + 2) % 4], tcol + dc[(d + 2) % 4]
                for nrow, ncol in tmp_loc:
                    visited[nrow][ncol] = 1
                check_room(cnt + 1)
                for nrow, ncol in tmp_loc:
                    visited[nrow][ncol] = 0


n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

ans = int(1e9)
cctvs = 0

for i in range(n):
    for j in range(m):
        if office[i][j] == 5:       # 4방향 모두 가능한 점부터 찾아서 처리해주기
            visited[i][j] = 1
            for d in range(len(dr)):
                ni, nj = i + dr[d], j + dc[d]
                while 0 <= ni < n and 0 <= nj < m and office[ni][nj] != 6:
                    visited[ni][nj] = 1
                    ni, nj = ni + dr[d], nj + dc[d]

check_idx = []
for i in range(n):
    for j in range(m):
        if 0 < office[i][j] < 5:        # 탐색 가능하다면
            cctvs += 1
            check_idx.append((office[i][j], i, j))

# 많이 탐색할 수 있는 애들부터 체킹해주기 위함
check_idx.sort(key=lambda x: x[0], reverse=True)

# 재귀 시작
check_room(0)

print(ans)