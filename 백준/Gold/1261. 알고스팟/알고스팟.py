'''
heapq
벽을 부순 개수를 첫번째 인자로 지정하여 벽을 부순 횟수가 낮은 것부터 가도록 하기
'''

import heapq, sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dijkstra():
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    visited[0][0] = 1
    while pq:
        move, row, col = heapq.heappop(pq)

        if (row, col) == (n - 1, m - 1):
            return move

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol]:
                if maze[nrow][ncol]:
                    heapq.heappush(pq, (move + 1, nrow, ncol))
                else:
                    heapq.heappush(pq, (move, nrow, ncol))
                visited[nrow][ncol] = 1


m, n = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

print(dijkstra())
