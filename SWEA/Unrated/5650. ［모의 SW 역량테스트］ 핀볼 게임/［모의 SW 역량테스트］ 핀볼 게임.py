'''
블록은 5가지로 존재한다.
핀볼 상하좌우 움직임
핀볼은 벽에 맞으면 반대로 이동한다.
웜홀 : 웜홀에 빠지면 동일한 숫자를 가진 다른 반대편 웜홀로 나온다.
    - 진행방향 그대로 유지
    - 6 ~ 10 숫자로 주어진다.
블랙홀 : 핀볼이 사라지며 게임 종료

게임은 핀볼이 출발 위치로 돌아오거나 블랙홀에 빠질 때 종료.
점수는 벽이나 블록에 부딪힌 횟수(웜홀은 점수 아님)

풀이:
시뮬레이션
벽을 잘 세팅해야 한다. dict and list로 세팅하기
    - next loc을 현재 벽 + nr, nc로 설정하기
    1번 : 아래 -> 오 , 왼 -> 위
    2번 : 위 -> 오, 왼 -> 아래
    3번 : 위 -> 왼, 오 -> 아래
    4번 : 아래 -> 왼, 오 -> 위
웜홀 : dict and list로 묶기
'''

#    오  아  왼  위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

walls = {1: [2, 0, 3, 1], 2: [2, 3, 1, 0], 3: [1, 3, 0, 2], 4: [3, 2, 0, 1], 5: [2, 3, 0, 1]}


def game_start(sr, sc, sd):
    tmp_ans = 0
    r, c, d = sr, sc, sd
    while True:
        nr, nc, nd = r + dr[d], c + dc[d], d

        # 격자 밖으로 나갔을 경우
        if not (0 <= nr < n and 0 <= nc < n):
            tmp_ans += 1
            nd = (d + 2) % 4
            r, c, d = nr, nc, nd
        else:
            obstacle = board[nr][nc]

            # 게임 종료
            if (nr, nc) == (sr, sc) or obstacle == -1:
                break

            # 벽에 박았다면
            if 1 <= obstacle <= 5:
                tmp_ans += 1
                nd = walls[obstacle][d]
            elif 6 <= obstacle <= 10:
                for i in range(len(wormholes[obstacle])):
                    if wormholes[obstacle][i] != (nr, nc):
                        nr, nc = wormholes[obstacle][i]
                        break

            r, c, d = nr, nc, nd

    return tmp_ans


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    wormholes = {}
    # 웜홀 찾기
    for i in range(n):
        for j in range(n):
            if 6 <= board[i][j] <= 10:
                if board[i][j] not in wormholes.keys():
                    wormholes.update({board[i][j]: [(i, j)]})
                else:
                    wormholes[board[i][j]].append((i, j))

    # 위치 완탐으로 찾기
    ans = 0
    for sr in range(n):
        for sc in range(n):
            if not board[sr][sc]:
                for d in range(len(dr)):
                    ans = max(ans, game_start(sr, sc, d))

    print(f"#{tc} {ans}")
