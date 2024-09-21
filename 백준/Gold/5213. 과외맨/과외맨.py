'''
홀수 줄에는 n개의 타일, 짝수 줄에는 n - 1개의 타일이 놓여져 있음
타일은 두 조각으로 나눠져 있음

한 타일에서 다른 타일로 넘어가려면 두 타일이 인접해야 하며, 같은 변을 공유하는 조각에 쓰인 숫자가 같아야 함
첫 번째 줄의 첫 타일의 번호는 1, 마지막 타일의 번호는 N이다. 두 번째 줄에서 첫 타일의 번호는 N+1이고, 마지막 타일의 번호는 2*N-1이다.

마지막 타일로 가지 못하는 경우, 번호가 가장 큰 타일로 이동하면 된다.(번호 큰 타일 값을 저장해야 함)

풀이:

- 타일 경로를 계산하는 dict 배열을 하나 만들자.
- 초기 사다리 배열에 저장할 때, (타일 번호, 값) 으로 저장하기
- bfs 이동 후 타일이 다른 경우만 거리 길이 비교해서 업데이트 시키기
'''


import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dijkstra(sr, sc):
    global endflag, max_tile
    pq = []
    heapq.heappush(pq, (0, sr, sc))  # (비용, 행, 열)
    visited[sr][sc] = 0

    while pq:
        cost, r, c = heapq.heappop(pq)
        cur_tile = tiles[r][c][0]

        if cost > visited[r][c]:
            continue

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < n and 0 <= nc < 2 * n):
                continue
            if tiles[nr][nc] == -1:
                continue
            # 타일 번호는 다르지만, 값이 다른 경우, continue
            new_tile = tiles[nr][nc][0]
            next_cost = cost
            if cur_tile != new_tile and tiles[r][c][1] != tiles[nr][nc][1]:
                continue
            # 만약 새로운 타일에 도착했다면, visited 하나 더 늘려주기
            if cur_tile != new_tile:
                next_cost += 1

            if visited[nr][nc] > next_cost:
                visited[nr][nc] = next_cost
                heapq.heappush(pq, (next_cost, nr, nc))
                move_dir[nr][nc] = (r, c)
                max_tile = max(max_tile, new_tile)
            # 만약 마지막 타일에 도착했다면, 플래그 on
            if new_tile == num:
                endflag = True
                return


n = int(input())
tiles = [[-1] * (2 * n) for _ in range(n)]
sr, sc, num = 0, 0, 0
for _ in range(n * n - n // 2):
    a, b = map(int, input().split())
    num += 1
    tiles[sr][sc], tiles[sr][sc + 1] = (num, a), (num, b)
    sc += 2
    if sr % 2 and sc > 2 * n - 2:
        sr, sc = sr + 1, 0
    elif not sr % 2 and sc > 2 * n - 1:
        sr, sc = sr + 1, 1

endflag = False
max_tile = 0
visited = [[int(1e9)] * (2 * n) for _ in range(n)]
move_dir = [[0] * (2 * n) for _ in range(n)]

dijkstra(0, 0)

# 경로 찾기(타일이 가장 큰 것 부터 찾아야함)
flag, ans = 0, []       # 경로 찾았는지 확인하는 flag
for i in range(n - 1, -1, -1):
    for j in range(2 * n - 1, -1, -1):
        if visited[i][j] != int(1e9):
            print(visited[i][j] + 1)
            ans.append(tiles[i][j][0])
            r, c = i, j
            while r > 0 or c > 0:
                nr, nc = move_dir[r][c]
                tile = tiles[nr][nc][0]
                if ans[-1] != tile:
                    ans.append(tile)
                r, c = nr, nc
            flag = 1
            break
    if flag:
        break

ans.reverse()
print(*ans)