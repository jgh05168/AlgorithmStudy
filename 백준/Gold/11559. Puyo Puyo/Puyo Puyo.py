'''
1. 우선적으로 뿌요가 존재하는 부분만 탐색.
2. 한 턴씩 동작 수행
    2-1. 그래프순회(bfs)를 하여 4개 이상이라면 터트리고 종료
    2-2. 터트릴 수 있다면 칸을 .으로 만들어주기
    2-3. 연쇄 += 1
    - 어차피 여러번 터져도 연쇄는 1만 증가하게 된다.
3. 남은 뿌요들 while문 사용하여 아래로 이동시켜주기
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol, deleted):
    queue = deque()
    temp_list = deque()
    queue.append((srow, scol))
    temp_list.append((srow, scol))
    cnt = 1
    visited[srow][scol] = 1
    color = field[srow][scol]

    while queue:
        row, col = queue.popleft()
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and field[nrow][ncol] == color and not visited[nrow][ncol]:
                cnt += 1
                visited[nrow][ncol] = 1
                queue.append((nrow, ncol))
                temp_list.append((nrow, ncol))

    if cnt >= 4:
        deleted.extend(list(temp_list))
        for drow, dcol in temp_list:
            field[drow][dcol] = '.'
        return 1, deleted
    else:
        return 0, deleted


def gravity():
    # 아래부터 탐색
    for i in range(N - 1, -1, -1):
        for j in range(M):
            if field[i][j] != '.':
                row, col = i, j
                while row < N:
                    nrow = row + 1
                    if nrow < N and field[nrow][col] == '.':
                        field[nrow][col] = field[row][col]
                        field[row][col] = '.'
                        row = nrow
                    else:
                        break


N, M = 12, 6
field = [list(input().rstrip()) for _ in range(N)]

# 1. 뿌요인 부분들 찾기
ppuyo_list = []
for i in range(N):
    for j in range(M):
        if field[i][j] != '.':
            ppuyo_list.append((i, j))
ppuyo_list.sort(key=lambda x:x[0], reverse=True)

total = 0
while True:
    visited = [[0] * M for _ in range(N)]
    ispang = 0
    deleted = []
    new_ppuyo_list = []
    for srow, scol in ppuyo_list:
        if not visited[srow][scol]:
            pang, deleted = bfs(srow, scol, deleted)
            ispang += pang

    if ispang:
        total += 1
        # 뿌요 내리기(전체 탐색)
        gravity()
        ppuyo_list = []
        for i in range(N):
            for j in range(M):
                if field[i][j] != '.':
                    ppuyo_list.append((i, j))
        ppuyo_list.sort(key=lambda x: x[0], reverse=True)
    else:
        break

print(total)