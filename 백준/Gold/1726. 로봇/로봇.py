'''
명령 1: GO k - k는 1, 2 또는 3 일 수 있다.
명령 2: Turn dir - dir는 왼/오 이며 회전한다.

주어진 위치까지 이동하고자 할 때 최소 명령을 구하자.

고려해야 할 사항 :
1. 회전을 어디서 어디로 하는지 - abs(현재 위치 - 바뀌는 위치)
2. 몇 칸이나 앞으로 이동하는지
visited 배열의 초기값 = 0 설정

bfs
----------- 우선순위 큐 사용 시 실패 ----------------
모든 동작에 대해 고려 & 4방향 각각에 대한 visited 사용
'''

from collections import deque
import sys
input = sys.stdin.readline

#    동  서  남  북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

scope = ((2, 3), (2, 3), (0, 1), (0, 1))


def bfs(srow, scol, sdir):
    queue = deque()
    queue.append((srow, scol, sdir, 0))
    visited[sdir][srow][scol] = 1

    while queue:
        row, col, direc, cnt = queue.popleft()

        if (row, col) == (erow - 1, ecol - 1) and direc == edir - 1:
            return cnt

        # 앞으로 나아가는 과정부터 진행(최대 3칸)
        for go in range(1, 4):
            nrow, ncol = row + dr[direc] * go, col + dc[direc] * go
            # 만약 벽을 만나거나 범위 밖이면 반복문 종료
            if not (0 <= nrow < N and 0 <= ncol < M) or factory[nrow][ncol]:
                break

            # 이미 방문한 곳이라면
            if visited[direc][nrow][ncol]:
                continue

            # 처음 방문이라면
            visited[direc][nrow][ncol] = 1
            queue.append((nrow, ncol, direc, cnt + 1))          # cnt를 직접 업데이트 해주는 것이 아니기 때문에, 3번 방문 이전에는 +1 된 것으로 취급된다.

        # 방향을 고려 - 모든 방향에 대해서 방문을 각각 해야 한다.
        for d in scope[direc]:          # 동/서 일 경우 남/북 에 대해서, 남/북 일 경우 동/서 에 대해서 조작 
            if not visited[d][row][col]:
                visited[d][row][col] = 1
                queue.append((row, col, d, cnt + 1))



N, M = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(N)]
srow, scol, sdir = map(int, input().split())
erow, ecol, edir = map(int, input().split())

visited = [[[0] * M for _ in range(N)] for _ in range(4)]

print(bfs(srow - 1, scol - 1, sdir - 1))
