import sys
sys.setrecursionlimit(10**6)        # 재귀 한도 넉넉하게 설정

T = int(input())

drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

# dfs(방문한 노드 리스트, 배추밭, 현재 row, 현재 col)
def dfs(visited, field, row, col):
    if visited[row][col] == True:       # 만약 방문했다면 그대로 반혼
        return
    else:                               # 방문하지 않았던 노드라면
        visited[row][col] = True        # 방문함으로 바꿔줌
        for d in range(len(drow)):      # 4방향에 대해서 조사(상/하/좌/우)
            nrow = row + drow[d]
            ncol = col + dcol[d]
            # 만약 nrow, ncol이 범위 안에 있고, 배추가 존재하며, 방문하지 않았던 곳이라면
            if 0 <= nrow < N and 0 <= ncol < M and field[nrow][ncol] == 1 and visited[nrow][ncol] == False:
                dfs(visited, field, nrow, ncol)     # dfs 수행(그래프 찾기 식)


for tc in range(1, T + 1):
    cnt = 0
    M, N, K = map(int, input().split())

    # 빈 밭 생성
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]       # 방문 위치 생성

    # 값을 하나씩 불러와 밭에 배추를 심는 과정
    for _ in range(K):
        col, row = map(int, input().split())
        field[row][col] = 1

    for row in range(N):
        for col in range(M):
            # 만약 인접 배추가 존재하고, 아직 방문하지 않은 곳이라면
            if field[row][col] == 1 and visited[row][col] == False:
                dfs(visited, field, row, col)   # dfs 수행
                cnt += 1                        # 모든 dfs 수행 후 군집을 생성하였기 때문에 cnt += 1

    print(cnt)