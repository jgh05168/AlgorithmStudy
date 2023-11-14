'''
말처럼 움직이는 경우 & 한 번씩 움직이는 경우에 대해서 따로 설정하여 deque에 저장

 -> 조건 설정이 필요
    1. k번 이하 만큼 움직였는가?
    2. 갈 수 있는 위치인가?

 - k의 범위 : 0 <= k <= 30
    -> visited 배열을 3차원으로 생성 & k개만큼 생성해도 가능하다.

deque에 (row, col, 말처럼 이동한 경우) 정보 저장
오른쪽 아래 도착하면 바로 return
'''

from collections import deque
import sys
input = sys.stdin.readline

horse_dr = [-1, 1, 2, 2, 1, -1, -2, -2]
horse_dc = [2, 2, 1, -1, -2, -2, -1, 1]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol, 0))
    visited[0][srow][scol] = 0

    while queue:
        row, col, horse_act = queue.popleft()

        # 말처럼 이동
        for d in range(len(horse_dr)):
            nrow, ncol = row + horse_dr[d], col + horse_dc[d]
            if 0 <= nrow < h and 0 <= ncol < w and k - horse_act > 0 and visited[horse_act + 1][nrow][ncol] == -1 and not grid[nrow][ncol]:
                if (nrow, ncol) == (h - 1, w - 1):
                    return visited[horse_act][row][col] + 1
                visited[horse_act + 1][nrow][ncol] = visited[horse_act][row][col] + 1
                queue.append((nrow, ncol, horse_act + 1))
        # 원숭이 이동
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < h and 0 <= ncol < w and visited[horse_act][nrow][ncol] == -1 and not grid[nrow][ncol]:
                if (nrow, ncol) == (h - 1, w - 1):
                    return visited[horse_act][row][col] + 1
                visited[horse_act][nrow][ncol] = visited[horse_act][row][col] + 1
                queue.append((nrow, ncol, horse_act))
    return -1


k = int(input())
w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
visited = [[[-1] * w for _ in range(h)] for _ in range(k + 1)]

if (w, h) == (1, 1):
    print(0)
else:
    print(bfs(0, 0))