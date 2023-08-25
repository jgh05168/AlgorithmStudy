# 최대 k 를 2 * N으로 설정
# 이전 k 안에 있던 집의 개수를 load하는 것이 관건이다.

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(queue):
    new_houses = 0
    cur_queue = queue   # 이전에 사용하기 위한 겉면의 좌표값 정보들을 불러온다.
    queue = []          # main에서 사용하는 큐 초기화
    while cur_queue:
        row, col = cur_queue.pop(0)
        for d in range(len(dr)):
            nrow = row + dr[d]
            ncol = col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol]:
                if mapp[nrow][ncol] == 1:
                    new_houses += 1             # 겉부분에 존재하는 집의 개수 count
                queue.append((nrow, ncol))
                visited[nrow][ncol] = True
    return new_houses, queue

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(N)]
    max_house = 0
    for i in range(N):
        for j in range(N):
            # 초기 bfs 설정
            dp = [0] * (N + N + 1)      # 집의 개수를 저장시켜주는 배열
            visited = [[False] * N for _ in range(N)]
            visited[i][j] = True
            queue = []                  # 겉면의 좌표 정보만을 저장하는 큐
            queue.append((i, j))

            # K = 1 일 경우 확인
            if mapp[i][j] == 1:
                dp[1] = 1
                price = (dp[1] * M) - 1
                if price >= 0 and max_house < dp[1]:
                    max_house = dp[1]

            # k 가 맵을 다 덮을 때인 2 + N 까지 반복하여
            # 회사가 이득을 볼 경우 최대 집의 개수를 세어준다.
            for k in range(2, 2 + N):
                new_houses, queue = bfs(queue)

                dp[k] = dp[k - 1] + new_houses
                price = (dp[k] * M) - (k * k + (k - 1) * (k - 1))
                if price >= 0 and max_house < dp[k]:
                    max_house = dp[k]

    print(f'#{tc} {max_house}')

