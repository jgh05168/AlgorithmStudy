'''
거울을 만날 경우, 경로를 바꿔줘야 한다.
양면거울이다.

빛을 문에서 다른 문으로 이동시키기

1. 거울이 활성화되었는가?
2. 빛이 이동한 경로가 맞는가?
3. 문에서 문으로 이동하였는가?

- 빛은 한 방향으로 이동한다.
- 거울을 만날 시 
    1. 거울을 사용하지 않는 경우
    2. 양방향으로 이동하는 경우

'''

import heapq, sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d_dict = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}

def dijkstra(srow, scol):
    pq = []
    for t in range(4):
        visited[t][srow][scol] = 0
        heapq.heappush(pq, (0, srow, scol, t))

    while pq:
        cost, row, col, d = heapq.heappop(pq)

        if (row, col) == (doors[1][0], doors[1][1]):
            return cost

        # 거울은 모든 방향으로 뻗어나가지 않음
        nrow, ncol = row + dr[d], col + dc[d]
        if 0 <= nrow < N and 0 <= ncol < N and room[nrow][ncol] != '*':
            if room[nrow][ncol] == '!':
                # 거울을 사용하는 경우
                new_cost = cost + 1
                for nd in d_dict[d]:
                    if visited[nd][nrow][ncol] > new_cost:
                        visited[nd][nrow][ncol] = new_cost
                        heapq.heappush(pq, (new_cost, nrow, ncol, nd))
                # 거울을 사용하지 않는 경우
            new_cost = cost
            nd = d
            if visited[nd][nrow][ncol] > new_cost:
                visited[nd][nrow][ncol] = new_cost
                heapq.heappush(pq, (new_cost, nrow, ncol, nd))


N = int(input())
room = [list(input().rstrip()) for _ in range(N)]
visited = [[[int(1e9)] * N for _ in range(N)] for _ in range(4)]

# 문 찾기
doors = []      # 행, 열, 방향 정보 순으로 저장
for i in range(N):
    for j in range(N):
        if room[i][j] == '#':
            doors.append((i, j))

print(dijkstra(doors[0][0], doors[0][1]))