'''
상근이의 존재에 대해 생각해야된다.

-> 감옥 외에 외부 공간을 새로 만들어주어 상근이가 원격으로 조종하는 경우에 대해서도 생각.
1. 상근이에 대해 우선순위 큐
2. 죄수 각각에 대해 우선순위 큐

- 만약 모두가 문을 연 경우라면, -2를 해주어서 중복을 제거해주면 된다.

문, 출구에 대한 값들 중 최솟값이 정답 !

'''

from collections import deque
import heapq, sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dijkstra(idx, srow, scol):
    pq = []
    heapq.heappush(pq, (0, srow, scol))
    visited[idx][srow][scol] = 0

    while pq:
        cur_cost, row, col = heapq.heappop(pq)

        if visited[idx][row][col] < cur_cost:
            continue

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < h + 2 and 0 <= ncol < w + 2 and visited[idx][nrow][ncol] == int(1e9) and jail[nrow][ncol] != '*':
                if jail[nrow][ncol] == '#':
                    new_cost = cur_cost + 1
                else:
                    new_cost = cur_cost
                visited[idx][nrow][ncol] = new_cost
                heapq.heappush(pq, (new_cost, nrow, ncol))


T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    jail = [['.'] + list(input().rstrip()) + ['.'] for _ in range(h)]
    jail.insert(0, (['.'] * (w + 2)))
    jail.append(['.'] * (w + 2))
    visited = [[[int(1e9)] * (w + 2) for _ in range(h + 2)] for _ in range(3)]

    prisoners = []
    idx = 0
    checked_loc = []
    for i in range(h + 2):
        for j in range(w + 2):
            if jail[i][j] == '$':
                prisoners.append((i, j))
                idx += 1

    # 상근이부터 돌아보기
    dijkstra(0, 0, 0)
    # 나머지 죄수들 돌아보기
    for idx in range(1, 3):
        dijkstra(idx, prisoners[idx - 1][0], prisoners[idx - 1][1])

    # 다 더한 뒤 -2씩 해준 뒤 최솟값 찾기
    min_v = int(1e9)
    for i in range(h + 2):
        for j in range(w + 2):
            temp = 0
            if jail[i][j] == '*':
                continue
            temp = visited[0][i][j] + visited[1][i][j] + visited[2][i][j]
            if jail[i][j] == '#':
                temp -= 2

            min_v = min(min_v, temp)
   
    print(min_v)