'''
복제 장치를 이용하면 자기 자신을 같은 로봇으로 원하는 개수만큼 복제 가능
미로에 로봇을 풀어둠 -> 흩어진 열쇠를 모두 찾는 게 목표

n x m
모든 열쇠를 찾으면서 로봇이 움직이는 횟수의 합을 최소로 하는 프로그램
상하좌우, 열쇠가 있는 위치에 도달했을 때 열쇠를 찾은 것
- 하나의 칸에 여러 로봇 위치가 가능
- 로봇이 움직인 횟수의 합 : 분열된 로봇이 각각 움직인 횟수의 총 합
- 열쇠만 찾으면 끝
250 x 50 x 50

풀이:
자신이 다시 지나갈 수 있는 조건 : 이동한 곳에서 열쇠를 찾았을 때
S에서는 무조건 복제
복제할 때마다, queue에 하나씩 추가한다.
'''

from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(sr, sc):
    pq = []
    heapq.heappush(pq, (0, sr, sc, 0))
    heapq.heappush(pq, (0, sr, sc, 1))
    visited[0][sr][sc] = 0
    visited[1][sr][sc] = 0
    total_robot = 1

    while pq:
        move, r, c, num = heapq.heappop(pq)

        # 한 노드에서 여러 개의 키를 찾는 경우, 복제된 로봇의 길이와 현재 간 길이를 재줘야 한다.
        find_key = []

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and visited[num][nr][nc] == -1:
                if grid[nr][nc] == '1':
                    continue
                if grid[nr][nc] == 'K':
                    if find_key:
                        noway = False
                        for nnr, nnc in find_key:
                            ndir = abs(nnr - nr) + abs(nnc - nc)
                            # 만약 복제된 로봇의 길이가 현재보다 짧다면, 굳이 현재 로봇은 업데이트 안해줘도 된다.
                            if ndir <= move + 1:
                                noway = True
                                break
                        if noway:
                            continue
                    # 아니라면, find_key에 현재 위치 넣어주기
                    find_key.append((nr, nc))
                    total_robot += 1    # 복제
                    heapq.heappush(pq, (0, nr, nc, total_robot))
                    visited.append([[-1] * n for _ in range(n)])
                    visited[total_robot][nr][nc] = 0
                    # 최소 키 찾기
                    if not min_keys[(nr, nc)]:
                        min_keys[(nr, nc)] = move + 1
                    else:
                        min_keys[(nr, nc)] = min(min_keys[(nr, nc)], move + 1)
                    # 먼저 찾은 키는 더이상 찾으면 안된다.
                    grid[nr][nc] = '0'
                else:
                    heapq.heappush(pq, (move + 1, nr, nc, num))
                    visited[num][nr][nc] = visited[num][r][c] + 1

    if len(min_keys) == m:
        return sum(min_keys.values())
    else:
        return -1


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    try:
        sc = grid[i].index('S')
        sr = i
        break
    except:
        continue

min_keys = defaultdict(int)
visited = [[[-1] * n for _ in range(n)] for _ in range(2)]
print(bfs(sr, sc))