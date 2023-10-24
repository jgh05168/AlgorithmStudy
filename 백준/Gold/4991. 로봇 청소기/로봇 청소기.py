'''
로봇 청소기

브루트포스 + bfs
쓰레기를 찾을 때마다 재귀 들어간다.
쓰레기에 대한 맵을 미리 생성. 찾은 쓰레기는 True 표시해주어 더이상 가지 못하도록 함
쓰레기를 찾지 못하는 경우에는 -1 출력
visited 배열은 재귀 들어갈 떄마다 새로 생성되어야 함
10 * 20 * 20
'''

from collections import deque
import sys
input = sys.stdin.readline


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(clean_trashes, total_move, srow, scol):
    queue = deque()
    queue.append((srow, scol))
    visited = [[-1] * M for _ in range(N)]      # 시초나면 아예 3차원 배열로 만들어서 시작해보기
    visited[srow][scol] = 0
    find = False

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and visited[nrow][ncol] == -1 and room[nrow][ncol] != 'x':
                if room[nrow][ncol] == '*':             # 쓰레기를 마주했다면
                    if not trash_map[nrow][ncol]:       # 이전에 방문한 쓰레기인지 확인
                        find = True
                        trash_map[nrow][ncol] = 1
                        # 다른 쓰레기를 치우러 가본다.
                        clean(clean_trashes + 1, (nrow, ncol), total_move + visited[row][col] + 1)
                        trash_map[nrow][ncol] = 0
                queue.append((nrow, ncol))
                visited[nrow][ncol] = visited[row][col] + 1

    return find

def clean(clean_trashes, robot, total_move):
    global min_move
    # 종료 조건
    if clean_trashes == total_trash:
        min_move = min(min_move, total_move)
        return

    # 가지치기
    if min_move < total_move:
        return

    # 쓰레기를 찾아가기 위한 bfs 진행
    find = bfs(clean_trashes, total_move, robot[0], robot[1])
    if not find:
        min_move = -1
        return


while True:
    M, N = map(int, input().split())
    if (N, M) == (0, 0):
        break
    room = [list(input().rstrip()) for _ in range(N)]
    trash_map = [[0] * M for _ in range(N)]
    min_move = 400
    total_trash = 0
    robot = (0, 0)

    # 로봇청소기 위치, 쓰레기 개수 세주기
    for i in range(N):
        for j in range(M):
            if room[i][j] == 'o':
                robot = (i, j)
                room[i][j] = '.'
            elif room[i][j] == '*':
                total_trash += 1

    # 재귀 시작
    clean(0, robot, 0)

    print(min_move)