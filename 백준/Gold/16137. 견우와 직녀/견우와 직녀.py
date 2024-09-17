'''
상하좌우, 1분씩 걸린다
일부 절벽에만 다리를 만들어 주고 있고, 그마저도 힘들어서 몇 분 주기로 오작교를 짓고 해체하는 작업을 반복한다.
한 번 지은 오작교는 1분 동안 유지 가능
두 번 연속 오작교 건너기 불가능

절벽을 정확히 하나 골라 주기가 m분인 오작교를 하나 더 놓아주기로 함
    - 이미 짓기로 예상한 절벽에는 더 놓을 수 없다.
    - 가로와 세로로 교차하는 곳에도 오작교를 지을 수 없음

10 x 10, 주기 : <= 20
(0, 0) -> (n - 1, n - 1)

풀이:
bfs, 다익스트라
오작교를 놓고 안놓고에 대해서 따로 visited를 해주어야 한다.
이전에 오작교를 건넜는지에 대한 정보 체크해야 함

'''

import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dijkstra(sr, sc):
    pq = []
    heapq.heappush(pq, (0, 0, 0, sr, sc))
    visited[0][sr][sc] = 0
    visit_list = [[[0] * n for _ in range(n)] for _ in range(2)]
    visit_list[0][0][0] = 1
    while pq:
        move, built, bridge_cross, r, c = heapq.heappop(pq)
        visit_list[built][r][c] = 0

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                # 모든 경우에서 도착지에 도착했다면
                if (nr, nc) == (n - 1, n - 1):
                    return move + 1
                # 오작교를 짓지 못하는 절벽이라면
                if grid[nr][nc] == -1:
                    continue
                # 만약 절벽을 만난 경우 && 오작교를 지을 수 있다면
                if not grid[nr][nc] and not built and not bridge_cross:
                    # 만약 주기가 되었고, 시간이 적고, 연속으로 건너는 게 아니라면
                    if not (move + 1) % m and visited[1][nr][nc] > visited[built][r][c] + 1:
                        if not visit_list[built + 1][nr][nc]:
                            visit_list[built + 1][nr][nc] = 1
                            heapq.heappush(pq, (move + 1, built + 1, 1, nr, nc))    # 건넜음 체크
                            visited[built + 1][nr][nc] = visited[built][r][c] + 1
                    # 아직 주기가 덜되었다면, 같은 장소에서 기다리기
                    else:
                        if not visit_list[built][r][c]:
                            visit_list[built][r][c] = 1
                            heapq.heappush(pq, (move + 1, built, 0, r, c))
                            visited[built][r][c] += 1
                # 만약 일반 길이라면,
                elif grid[nr][nc] == 1 and visited[built][nr][nc] > visited[built][r][c] + 1:
                    if not visit_list[built][nr][nc]:
                        visit_list[built][nr][nc] = 1
                        heapq.heappush(pq, (move + 1, built, 0, nr, nc))
                        visited[built][nr][nc] = visited[built][r][c] + 1
                # 만약 오작교를 만났다면,
                elif grid[nr][nc] > 1 and not bridge_cross:
                    if not (move + 1) % grid[nr][nc] and visited[built][nr][nc] > visited[built][r][c] + 1:
                        if not visit_list[built][nr][nc]:
                            visit_list[built][nr][nc] = 1
                            heapq.heappush(pq, (move + 1, built, 1, nr, nc))
                            visited[built][nr][nc] = visited[built][r][c] + 1
                    else:
                        if not visit_list[built][r][c]:
                            visit_list[built][r][c] = 1
                            heapq.heappush(pq, (move + 1, built, 0, r, c))
                            visited[built][r][c] += 1


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 다리 못놓는 곳은 미리 체크
for i in range(n):
    for j in range(n):
        if not grid[i][j]:
            adj_check = False
            for d in range(len(dr)):
                nr, nc = i + dr[d], j + dc[d]
                nnr, nnc = i + dr[(d + 1) % 4], j + dc[(d + 1) % 4]
                if 0 <= nr < n and 0 <= nc < n and 0 <= nnr < n and 0 <= nnc < n:
                    if not grid[nr][nc] and not grid[nnr][nnc]:
                        adj_check = True
                        break
            if adj_check:
                grid[i][j] = -1

visited = [[[int(1e5)] * n for _ in range(n)] for _ in range(2)]
print(dijkstra(0, 0))