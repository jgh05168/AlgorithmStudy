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
--------------------------------------
주사위를 배열로 정해주지 말고, 값을 바로바로 업데이트 해주기(하드코딩)
'''

from collections import deque
import sys
input = sys.stdin.readline

# 동 남 서 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def rotate(d):
    global top, bottom, east, west, south, north
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
    b = board[nr][nc]
    if bottom > b:
        return (d + 1) % 4
    elif bottom < b:
        return (d - 1) % 4
    else:
        return d


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
r, c, d = 0, 0, 0

# 주사위 눈 정하기
top = 1
bottom = 6
east = 3
west = 4
north = 2
south = 5

ans = 0
for _ in range(k):
    # 0. 이동 방향으로 한 칸 굴리기
    nr, nc = r + dr[d], c + dc[d]
    if not (0 <= nr < n and 0 <= nc < m):
        d = (d + 2) % 4
        nr, nc = r + dr[d], c + dc[d]

    # 1. 주사위 이동
    rotate(d)

    # 2. 점수 획득
    ans += bfs(nr, nc, board[nr][nc])

    # 3. 방향 비교
    d = get_direction()

    r, c = nr, nc

print(ans)