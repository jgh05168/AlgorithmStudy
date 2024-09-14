'''
n x m, 빈칸 / 장애물
보드의 빈 칸 위에 공을 하나 놓으면 시작한다.
1. 동서남북 중 한 방향을 고른 다음, 그 방향으로 계속 이동시킨다.
2. 공은 장애물, 보드의 경계, 이미 공이 지나갔던 칸을 만나기 전까지 계속해서 이동한다.
    - 게임은 공이 더 이상 이동할 수 없을 때 끝난다.
    - 이 때, 모든 빈 칸을 공이 방문한 적이 있어야 한다.
이동 횟수의 최솟값을 구하자

풀이:
dfs -> 정해진 방향에 대해서 쭉 이동해보기.
    - 이후 막힌다면, dfs로 들어가기
        - 못가는 방향 정보고 넣어줘야 한다.
    - 4 x 30 x 30
    - 종료 조건 : 막힌 곳에서 더 이상 이동할 곳이 없을 때.
빈 칸 개수를 체크해주어야 한다.
방문한 칸 누적해서 비교하기
'''

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(depth, visit_cnt, sr, sc):
    global ans
    if depth > ans:
        return
    flag = 0
    for d in range(len(dr)):
        cango_list = []
        # 갈 수 있는 경우까지 계속 가기
        r, c = sr, sc
        nr, nc = r, c
        while True:
            nr, nc = r + dr[d], c + dc[d]
            # 못 가는 조건
            if not (0 <= nr < n and 0 <= nc < m) or board[nr][nc] == '*' or visited[nr][nc]:
                break
            # 갈 수 있다면,
            cango_list.append((nr, nc))
            r, c = nr, nc
        if cango_list:
            flag = 1
            for nr, nc in cango_list:
                visited[nr][nc] = 1
            dfs(depth + 1, visit_cnt + len(cango_list), r, c)
            for nr, nc in cango_list:
                visited[nr][nc] = 0

    # 만약 한 방향도 못 갔다면
    if not flag:
        # 값 업데이트 해줘야함
        if visit_cnt == cango_place:
            ans = min(ans, depth)


tc = 1
while True:
    try:
        n, m = map(int, input().split())
        board = [list(input().rstrip()) for _ in range(n)]
        cango_place = n * m
        for i in range(n):
            for j in range(m):
                if board[i][j] == '*':
                    cango_place -= 1

        ans = 1000001
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    visited = [[0] * m for _ in range(n)]
                    visited[i][j] = 1
                    dfs(0, 1, i, j)   # depth, visit
                    visited[i][j] = 0
        if ans == 1000001:
            ans = -1
        print(f'Case {tc}: {ans}')
        tc += 1

    except:
        break
