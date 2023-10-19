'''
한 칸 씩 이동하고, 맵 업데이트하고, 반복
    - 한 칸 위를 확인하여 내려올 수 있는지 여부를 판단하기.
만약 움직일 수 있는 경우가 없으면 못감 리턴
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 1, 1, 0, -1, -1, -1, 0]
dc = [1, 1, 0, -1, -1, -1, 0, 1, 0]

def bfs(srow, scol):
    visited = [[0] * n for _ in range(n)]
    visited[srow][scol] = 1
    temp_queue = deque()
    temp_queue.append([(srow, scol)])

    while temp_queue:

        queue = deque(temp_queue.popleft())
        temp_list = []
        while queue:
            row, col = queue.popleft()

            # 여덟방향 움직이기
            for d in range(len(dr)):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 <= nrow < n and 0 <= ncol < n and board[nrow][ncol] == '.':
                    if (nrow, ncol) == (0, n - 1):
                        return 1
                    if nrow - 1 >= 0 and board[nrow - 1][ncol] == '.':
                        if (nrow, ncol) == (row, col) or not visited[nrow][ncol]:
                            visited[nrow][ncol] = 1
                            temp_list.append((nrow, ncol))

        # 갈 수 있는 곳이 없다면 종료
        if temp_list == []:
            break
        # 다 움직였으면 맵 업데이트
        board.appendleft(['.'] * n)
        board.pop()

        temp_queue.append(temp_list)

    return 0


n = 8
board = deque([list(input().rstrip()) for _ in range(n)])

ans = bfs(n - 1, 0)
print(ans)
