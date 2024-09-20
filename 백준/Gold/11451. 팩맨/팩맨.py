'''
팩맨 2마리는 서로 다른 위치에 있지만, 이동 방향을 공유한다.
자신의 앞에 벽이 있으면 이동하지 않는다.
- 팩맨을 한 장소로 합치는 것에만 집중하기

방문 처리는 어떻게 ?
    - 두 팩맨이 모두 방문했던 곳이라면 이동 막기
    - dict로 이동 여부 판단하기
'''

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
order_dict = {0: 'E', 1: 'S', 2: 'W', 3: 'N'}

def bfs(sloc):
    queue = deque()
    queue.append((sloc, ""))

    while queue:
        p, order = queue.popleft()
        # 도착점인 경우 경로 return
        p1, p2 = p
        if p1 == p2:
            return order
        r1, c1 = p1
        r2, c2 = p2

        for d in range(len(dr)):
            tmp_order = [s for s in order]
            nr1, nc1 = (r1 + dr[d]) % n, (c1 + dc[d]) % m
            nr2, nc2 = (r2 + dr[d]) % n, (c2 + dc[d]) % m
            # 이미 방문했다면
            if visited.get(((nr1, nc1), (nr2, nc2))):
                continue
            # 만약 유령을 만나면, continue
            if grid[nr1][nc1] == 'G' or grid[nr2][nc2] == 'G':
                continue
            # 둘 다 빈 공간이라면
            elif grid[nr1][nc1] == '.' and grid[nr2][nc2] == '.':
                tmp_order.append(order_dict[d])
                queue.append((((nr1, nc1), (nr2, nc2)), "".join(tmp_order)))
                visited[((nr1, nc1), (nr2, nc2))] = 1
            # 벽을 만난 경우
            else:
                tmp_order.append(order_dict[d])
                # p1이 벽에 걸린 경우
                if grid[nr1][nc1] == 'X' and grid[nr2][nc2] == '.':
                    # 이미 방문했다면, continue
                    if visited.get(((r1, c1), (nr2, nc2))):
                        continue
                    queue.append((((r1, c1), (nr2, nc2)), "".join(tmp_order)))
                    visited[((r1, c1), (nr2, nc2))] = 1
                # p2가 벽에 걸린 경우
                elif grid[nr1][nc1] == '.' and grid[nr2][nc2] == 'X':
                    if visited.get(((nr1, nc1), (r2, c2))):
                        continue
                    queue.append((((nr1, nc1), (r2, c2)), "".join(tmp_order)))
                    visited[((nr1, nc1), (r2, c2))] = 1
                else:
                    if visited.get(((r1, c1), (r2, c2))):
                        continue
                    queue.append((((r1, c1), (r2, c2)), "".join(tmp_order)))
                    visited[((r1, c1), (r2, c2))] = 1

    return "IMPOSSIBLE"


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(n)]

    # 팩맨 위치 찾기
    pacmans = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'P':
                pacmans.append((i, j))
                grid[i][j] = '.'

    pacmans = tuple(pacmans)
    visited = defaultdict(int)
    visited[pacmans] = 1

    final_order = bfs(pacmans)
    if final_order == "IMPOSSIBLE":
        print(final_order)
    else:
        print(len(final_order), final_order)