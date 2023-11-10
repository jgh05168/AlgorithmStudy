'''
방향을 비트마스킹으로 표현
if not i and (1 << d) 이런식 ?

나머지는 visited로 판단한다.

1. 이 성에 있는 방의 개수
2. 가장 넓은 방의 넓이
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
    -> 전체 for 문 다시 한 번 돌면서 벽이 있는 경우에 대해서 한 번 씩 더한 뒤 max로 업데이트
'''

from collections import deque
import sys
input = sys.stdin.readline

#    서  북  동  남
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def bfs(srow, scol, room_cnt):
    global largest_room
    queue = deque()
    queue.append((srow, scol))
    visited[srow][scol] = 1
    cnt = 1
    room_list = set()
    room_list.add((srow, scol))
    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            if not (castle[row][col] & (1 << d)):       # 벽에 막혀있지 않은 경우만 지나갈 수 있다.
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol]:
                    visited[nrow][ncol] = cnt + 1
                    queue.append((nrow, ncol))
                    cnt += 1
                    room_list.add((nrow, ncol))

    for rrow, rcol in room_list:
        room_number[rrow][rcol] = cnt
        divide_rooms[rrow][rcol] = room_cnt

    largest_room = max(largest_room, cnt)

m, n = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
room_number = [[0] * m for _ in range(n)]
divide_rooms = [[0] * m for _ in range(n)]

room_cnt = 0     # 성에 있는 방의 개수
largest_room = 0        # 가장 넓은 방의 넓이
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            room_cnt += 1
            bfs(i, j, room_cnt)

# 벽 하나 뚫었을 떄 가장 큰 방 넓이 구하기
max_expand_room = 0
for row in range(n):
    for col in range(m):
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and divide_rooms[nrow][ncol] != divide_rooms[row][col]:
                max_expand_room = max(max_expand_room, room_number[nrow][ncol] + room_number[row][col])

print(room_cnt)
print(largest_room)
print(max_expand_room)