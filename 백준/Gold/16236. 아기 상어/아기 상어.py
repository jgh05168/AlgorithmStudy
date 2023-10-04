'''
처음 아기상어 크기 = 2
아기상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

- 자신의 크기보다 큰 물고기는 지나갈 수 없다
- 자신의 크기보다 작은 물고기만 먹을 수 있다.

이동 방법

- 더 이상 먹을 수 있는 물고기가 없다면 종료
- 먹을 수 있는 물고기가 한마리라면 그 물고기를 먹으러 간다
- 먹을 수 있는 물고기가 한마리 이상이라면 거리가 가까운 물고기를 먹으러 간다.
    - 거리는 row, col 순으로 먹는다.
- 물고기를 먹으면 빈 칸이 된다.

bfs

물고기를 먹을 때마다 위치를 업데이트 해주고, bfs를 다시 진행해야한다.
우선순위 큐를 사용한다. - (물고기 크기, row, col 순서로 저장)

'''

import heapq, sys
input = sys.stdin.readline


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol):
    global size
    global total_time
    global cnt
    pq = []
    heapq.heappush(pq, (0, srow, scol, 0))
    visited[srow][scol] = 0

    while pq:
        dist, row, col, fish_size = heapq.heappop(pq)

        # 엄마 도움이 필요한 경우
        if fish_size > size:
            return True, row, col

        # 만약 물고기를 먹을 수 있다면
        # 먹고 위치 값 업데이트 후 다시 bfs 시도
        if 0 < fish_size < size:
            total_time += dist
            ocean[srow][scol] = 0       # 이전 상어 위치 초기화
            ocean[row][col] = 9         # 현재 상어 위치 업데이트
            cnt += 1        # 몸집 키우기
            return False, row, col

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and visited[nrow][ncol] == -1:
                if ocean[nrow][ncol] <= size:       # 자신이랑 크기가 같거나 작은 경우에만 이동 가능
                    visited[nrow][ncol] = visited[row][col] + 1
                    heapq.heappush(pq, (visited[nrow][ncol], nrow, ncol, ocean[nrow][ncol]))

    return True, row, col



N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]

if sum(map(sum, ocean)) == 9:   # 아기상어만 존재하는 경우
    print(0)                    # 종료

else:
    # 초반 상어 위치 찾기
    srow, scol = 0, 0
    for i in range(N):
        for j in range(N):
            if ocean[i][j] == 9:
                srow, scol = i, j
                break

    total_time = 0
    size = 2
    cnt = 0
    while True:
        if sum(map(sum, ocean)) == 9:       # 먹을 수 있는 물고기를 다 먹었다면 프로그램 종료
            break

        visited = [[-1] * N for _ in range(N)]
        call_mom, row, col = bfs(srow, scol)
        srow, scol = row, col

        if cnt == size:     # 자기 사이즈만큼 물고기 수를 먹었다면 사이즈 증가
            size += 1
            cnt = 0

        if call_mom:
            break

    print(total_time)