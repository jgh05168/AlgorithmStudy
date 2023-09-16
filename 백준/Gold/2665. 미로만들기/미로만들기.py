'''
벽이 아닌 부분을 우선적으로 큐에 삽입
visited : 벽의 개수를 count

'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol))
    visited[srow][scol] = 0

    while queue:
        row, col = queue.popleft()
        if (row, col) == (n - 1, n - 1):
            return visited[row][col]
        else:
            for d in range(len(dr)):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 <= nrow < n and 0 <= ncol < n and visited[nrow][ncol] == -1:
                    # 흰 방일 경우
                    if rooms[nrow][ncol]:
                        visited[nrow][ncol] = visited[row][col]
                        queue.appendleft((nrow, ncol))
                    # 검은방일 경우
                    else:
                        visited[nrow][ncol] = visited[row][col] + 1
                        queue.append((nrow, ncol))


# inputs
n = int(input())
rooms = [list(map(int, input().rstrip())) for _ in range(n)]

# 출발지 : 0, 0
# 도착지 : n - 1, n - 1
# 출발지와 도착지는 흰 방으로 구성
# 흰 방 : 1, 검은 방 : 0
visited = [[-1] * n for _ in range(n)]
print(bfs(0, 0))

