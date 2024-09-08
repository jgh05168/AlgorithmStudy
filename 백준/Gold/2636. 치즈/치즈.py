'''
판의 가장자리에는 치즈가 놓여있지 않다.

치즈의 겉면부터 녹아 없어진다.
모두 녹아 없어지는 데 걸리는 시간, 녹기 한 시간 전에 남아있는 치즈 조각의 칸 수를 출력

100 x 100 x 4

풀이:
1. 치즈 겉면 정보를 저장 -> 0, 0에서 bfs써서 찾아내기(하나라도 닿는 치즈가 있으면 그놈은 겉면임)
2. while문 시작
    2-1. 겉면 녹이고, 주변에 붙어있는 치즈가 있다면 새로운 겉면에 추가
    2-2. 겉면 정보를 저장해주기 -> 녹기 한 시간 전 치즈 조각의 칸 수
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def get_cheese(list):
    queue = deque()
    for sr, sc in list:
        queue.append((sr, sc))
        visited[sr][sc] = 1

    cheese_space = set()
    while queue:
        r, c = queue.popleft()

        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                # 치즈이면,
                if grid[nr][nc]:
                    cheese_space.add((nr, nc))
                    grid[nr][nc] = 0
                else:
                    queue.append((nr, nc))
                visited[nr][nc] = 1

    return cheese_space


def get_new_cheese():
    new_cheese_space = set()
    for r, c in cheese_space:
        for d in range(len(dr)):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc]:
                new_cheese_space.add((nr, nc))
                visited[nr][nc] = 1
    return new_cheese_space


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 1. 치즈 겉면 정보 저장
cheese_space = get_cheese([(0, 0)])

last_space = len(cheese_space)
time = 0
while cheese_space:
    # 2. 새로운 치즈 영역 찾기 & 빈 치즈 영역 확장
    new_cheese_space = get_cheese(list(cheese_space))
    # 3.

    last_space = len(cheese_space)
    time += 1
    cheese_space = new_cheese_space

print(time)
print(last_space)
