from collections import deque
import sys
input = sys.stdin.readline

'''
먼저 토마토 틀을 전체 탐색해본다.
익은 토마토가 있는 경우, 없는 경우, 토마토가 아예 없는 경우를 나누어서 판단.
'''

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(riped):
    global tomatoes
    while riped:
        row, col = riped.popleft()
        tomatoes += 1
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < M and tray[nrow][ncol] == 0:
                tray[nrow][ncol] = tray[row][col] + 1
                riped.append((nrow, ncol))


M, N = map(int, input().split())
tray = [list(map(int, input().split())) for _ in range(N)]
riped = deque([])

riped_tomatoes = 0      # 익은 토마토 개수
unriped_tomatoes = 0    # 안익은 토마토 개수
# 토마토 정보들 확인
for i in range(N):
    for j in range(M):
        if tray[i][j] == 1:
            riped.append((i, j))
            riped_tomatoes += 1
        elif tray[i][j] == 0:
            unriped_tomatoes += 1

total_tomatoes = riped_tomatoes + unriped_tomatoes      # 전체 토마토 개수

tomatoes = 0

# 모두 익지 않은 토마토이거나, 토마토가 없느 경우
if not riped_tomatoes:
    print(-1)
# 잘 익은 토마토가 있는 경우
else:
    # 만약 저장될 때부터 모든 토마토가 익어있는 상태라면
    if riped_tomatoes == total_tomatoes:
        print(0)
    # 몇 개만 익어있다면
    else:
        bfs(riped)      # 익은 토마토들에 대해서 bfs
                        # 이미 익은 토마토들의 그리드가 저장되어 있으므로 익은 것부터 bfs를 돌게 된다
                        # 따라서 모두 탐색할 경우에 가장 큰 값이 최대 일 수가 된다.
        if tomatoes == total_tomatoes:      # 전체 토마토의 수 = 현재 토마토의 수
            print(max(map(max, tray)) - 1)       # 토마토가 모두 익었다는 뜻
        else:
            print(-1)
