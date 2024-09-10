'''
n x m
주사위의 각 면 : 1 ~ 6 숫자가 있음
초기 주사위 전개도 정해짐
    - 주사위 지도 위에 윗 면이 1, 아랫면이 6
처음 주사위의 이동 방향은 동쪽, (0, 0) 시작
이동 한 번 방식
1. 주사위의 이동 방향으로 한 칸 굴러간다.
    - 만약 이동 방향에 칸이 없다면, 방향을 반대로 한 다음, 한 칸 구른다.
2. 주사위가 도착한 칸의 점수를 획득한다.
3. 주사위의 아랫면에 있는 정수(a)와 주사위 칸 정수(b)를 비교해 이동방향 결정
    - a > b : 90도 시계방향
    - a < b : 90도 반시계방향
    - a = b : 이동 방향 변화 x
점수 산정 : 연속해서 이동할 수 있는 칸 수 x 현재 좌표와 같은 값

풀이:
1. 주사위 동/서, 남/북 이동 방향 결정해줘야댐
2. 주사위 아랫면 : 주사위 좌표 (3, 1)
3. 이동하면 점수 산정을 위한 bfs 진행
4. 이동방향 결정
'''

from collections import deque
import sys
input = sys.stdin.readline

# 동 남 서 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

row_dir = [(1, 0), (1, 1), (1, 2), (3, 1)]
col_dir = [(0, 1), (1, 1), (2, 1), (3, 1)]


def rotate(sd):
    new_dice = [[0] * 3 for _ in range(4)]
    # 동
    if not sd:
        for i in range(len(row_dir)):
            r, c = row_dir[i]
            nr, nc = row_dir[(i + 1) % 4]
            new_dice[nr][nc] = dice[r][c]
    # 남
    elif sd == 1:
        for i in range(len(col_dir)):
            r, c = col_dir[i]
            nr, nc = col_dir[(i + 1) % 4]
            new_dice[nr][nc] = dice[r][c]
    # 서
    elif sd == 2:
        for i in range(len(row_dir)):
            r, c = row_dir[i]
            nr, nc = row_dir[(i - 1) % 4]
            new_dice[nr][nc] = dice[r][c]
    # 북
    else:
        for i in range(len(col_dir)):
            r, c = col_dir[i]
            nr, nc = col_dir[(i - 1) % 4]
            new_dice[nr][nc] = dice[r][c]

    # 나머지 주사위 완성하기
    for i in range(4):
        for j in range(3):
            if not new_dice[i][j] and dice[i][j]:
                new_dice[i][j] = dice[i][j]

    return new_dice


def bfs(sr, sc, val):
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    queue.append((sr, sc))
    visited[sr][sc] = 1

    tmp = 1
    while queue:
        r, c = queue.popleft()
        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc] == val:
                queue.append((nr, nc))
                visited[nr][nc] = 1
                tmp += 1
    return tmp * val


def get_direction():
    a, b = dice[dice_bottom[0]][dice_bottom[1]], board[nr][nc]
    if a > b:
        return (d + 1) % 4
    elif a < b:
        return (d - 1) % 4
    else:
        return d


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
r, c, d = 0, 0, 0
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
dice_bottom = (3, 1)

ans = 0
for _ in range(k):
    # 0. 이동 방향으로 한 칸 굴리기
    nr, nc = r + dr[d], c + dc[d]
    if not (0 <= nr < n and 0 <= nc < m):
        d = (d + 2) % 4
        nr, nc = r + dr[d], c + dc[d]

    # 1. 주사위 이동
    dice = rotate(d)

    # 2. 점수 획득
    ans += bfs(nr, nc, board[nr][nc])

    # 3. 방향 비교
    d = get_direction()

    r, c = nr, nc

print(ans)

################## dp를 사용한 풀이(참고함) ########################
'''
# BFS, 구현, 시뮬레이션
# 메모이제이션(또는 dp) <- 선택 : 일단 없이 브루트포스

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 오른 밑 왼 위, 시계방향+1, 반시계방향-1

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score = [[0] * m for _ in range(n)]
head = [[None] * m for _ in range(n)]  # visited 대신 대표 위치 저장
oob = [[False] * m + [True] for _ in range(n)] + [[True] * m]

for i in range(n):
    for j in range(m):
        if not head[i][j]:
            head[i][j] = (i, j)
            num = board[i][j]
            q = [(i, j)]
            cnt = 1
            while q:
                nq = []
                for x, y in q:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if not oob[nx][ny] and not head[nx][ny] and board[nx][ny] == num:
                            head[nx][ny] = (i, j)
                            cnt += 1
                            nq.append((nx, ny))
                q = nq
            score[i][j] = num * cnt
        else:
            hi, hj = head[i][j]
            score[i][j] = score[hi][hj]

d = 0
cx, cy = 0, 0

top = 1
bottom = 6
east = 3
west = 4
north = 2
south = 5

ans = 0

for roll in range(k):
    dx, dy = directions[d]
    nx, ny = cx + dx, cy + dy

    # 밖으로 나가려고하면 반대방향
    if oob[nx][ny]:
        d = (d + 2) % 4
        dx, dy = directions[d]
        nx, ny = cx + dx, cy + dy
    cx, cy = nx, ny

    # 미리 구해둔 점수
    ans += score[cx][cy]

    # 동쪽
    if not d:
        top, east, bottom, west = west, top, east, bottom
    # 남쪽
    elif d == 1:
        top, south, bottom, north = north, top, south, bottom
    # 서쪽
    elif d == 2:
        top, west, bottom, east = east, top, west, bottom
    # 북쪽
    else:
        top, north, bottom, south = south, top, north, bottom

    # 밑면과 판의 숫자 비교 후 방향 전환
    num = board[cx][cy]
    if bottom > num:
        d = (d + 1) % 4
    elif bottom < num:
        d = (d - 1) % 4

print(ans)

'''
