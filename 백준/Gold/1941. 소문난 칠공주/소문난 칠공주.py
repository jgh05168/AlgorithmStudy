'''
1941. 소문난 칠공주

1. 7명의 여학생으로 구성
2. 가로나 세로로 반드시 인접해야 함
3. 학생은 섞일 수 있되, 4명 이상의 이다솜파가 있어야 한다.

풀이:
dfs(조합) + bfs
1. 5 x 5에서 7개의 좌표를 조합으로 선택한다. (25C7 = 480700)
2. 이후 bfs로 뽑은 좌표를 돌며, 이어지는지 이어지지 않는지 체크한다.
    - 만약 이어지지 않거나, 이다솜파가 더 작으면 return false
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(loc):
    doyeon = 0
    for r, c in loc:
        if classroom[r][c] == 'Y':
            doyeon += 1
        if doyeon > 3:
            return False

    queue = deque([loc[0]])
    visited_bfs = [[0] * n for _ in range(n)]
    visited_bfs[loc[0][0]][loc[0][1]] = 1

    adj = 1
    while queue:
        r, c = queue.popleft()

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited_bfs[nr][nc] and visited[nr][nc]:
                queue.append((nr, nc))
                visited_bfs[nr][nc] = 1
                adj += 1
    if adj != 7:
        return False
    return True


def dfs(r, c, depth, loc):
    global ans
    if depth == 7:
        if bfs(loc):
            ans += 1
        return
    else:
        for i in range(r, n):
            if i != r:
                c = -1
            for j in range(c + 1, n):
                if not visited[i][j]:
                    visited[i][j] = 1
                    dfs(i, j, depth + 1, loc + [(i, j)])
                    visited[i][j] = 0


n = 5
classroom = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]
ans = 0
dfs(0, -1, 0, [])       # r, c, depth

print(ans)