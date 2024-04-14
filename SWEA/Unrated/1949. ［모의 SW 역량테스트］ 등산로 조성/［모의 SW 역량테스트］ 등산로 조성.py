'''
- 최대한 긴 등산로를 만들 것.
- 각 숫자는 지형의 높이를 나타냄
1. 가장 높은 봉우리에서 시작한다
2. 반드시 높은 지형에서 낮은 지형으로 상하좌우로 연결되야 함
3. 딱 한곳을 정해서 최대 k 깊이만큼 지형을 깎는 공사가 가능

n <= 8, k <= 5 충분히 깎고 들어갈 수 있을 것 같음

풀이:
dfs 진행
- 자기보다 높은 봉우리를 만날 경우, 5번 bfs 돌리기.
    - 인자로 깎을 수 있는지 없는지를 전달
    - 더이상 못깎는 경우 최대 등산로 갱신


'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(mountain, row, col, can_dig):
    global max_v

    for d in range(len(dr)):
        nrow, ncol = row + dr[d], col + dc[d]
        if 0 <= nrow < n and 0 <= ncol < n and not visited[can_dig][nrow][ncol]:
            # 현재보다 높은 경우
            if mountain[nrow][ncol] >= mountain[row][col]:
                # 만약 아직 dig를 안했다면
                if not can_dig:
                    for degree in range(1, k + 1):
                        mountain[nrow][ncol] -= degree
                        visited[1][row][col] = visited[0][row][col]
                        dfs(mountain, row, col, 1)
                        visited[1][row][col] = 0
                        mountain[nrow][ncol] += degree
                else:
                    max_v = max(max_v, visited[can_dig][row][col])
            # 그냥 갈 수 있다면 네 방향 중 가장 큰 값을 queue에 저장
            else:
                visited[can_dig][nrow][ncol] = visited[can_dig][row][col] + 1
                dfs(mountain, nrow, ncol, can_dig)
                visited[can_dig][nrow][ncol] = 0



T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]
    start_locs = []

    max_height = max(map(max, mountain))
    # print(max_height)
    for i in range(n):
        for j in range(n):
            if mountain[i][j] == max_height:
                start_locs.append((i, j))
    max_v = 0

    for sr, sc in start_locs:
        visited = [[[0] * n for _ in range(n)] for _ in range(2)]
        visited[0][sr][sc] = 1
        dfs(mountain, sr, sc, 0)

    print(f'#{t} {max_v}')