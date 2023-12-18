'''
초록색 배양액과 빨간색 배양액
배양액을 뿌릴 수 있는 땅은 미리 정해져있음
    - 뿌릴 수 있는 칸, 없는 칸, 호수

- 초록색 배양액과 빨간색 배양액이 동일한 시간에 도달한 땅에서는 꽃이 피어난다.
    - 이 땐 배양액이 사라지기 때문에 더이상 퍼뜨리지 않는다.
    - 다른 시간에 겹쳐진다면 꽃 x

꽃의 최대 개수 구하기 = 브루트포스, 순열, bfs
- 각각을 개별 배양액으로 판단하기

! 조합을 짤 경우가 생긴다면, itertools의 combinations를 사용하기
'''

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(media_loc):
    queue = deque(media_loc)
    visited = [[(-1, 0)] * m for _ in range(n)]
    for sidx in range(len(media_loc)):
        srow, scol = media_loc[sidx]
        visited[srow][scol] = (0, check_media[sidx])
    flowers = 0
    while queue:
        row, col = queue.popleft()
        # 만약 꽃이 되었다면 continue
        if visited[row][col][1] == 3:
            continue
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and garden[nrow][ncol]:
                if visited[nrow][ncol][0] == -1:
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = (visited[row][col][0] + 1, visited[row][col][1])
                elif visited[nrow][ncol][0] == visited[row][col][0] + 1 and visited[nrow][ncol][1] != visited[row][col][1]:
                    flowers += 1
                    visited[nrow][ncol] = (int(1e9), 3)

    return flowers



def per(cnt, pos, green, red):
    global max_flower
    if cnt == g + r:
        max_flower = max(max_flower, bfs(pos))
        return

    # 초록액 먼저 뿌려보기
    if green > 0:
        check_media[cnt] = 1
        per(cnt + 1, pos, green - 1, red)

    # 빨간액 뿌리기
    if red > 0:
        check_media[cnt] = 2
        per(cnt + 1, pos, green, red - 1)


n, m, g, r = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(n)]

culture_media = []
max_flower = 0
for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:
            culture_media.append((i, j))
check_media = [0] * (g + r)     # 무슨 색의 배양액을 뿌렸는지 알려주는 배열

# combination(위치, 개수) : 배양액을 넣을 수 있는 칸 중 넣을 배양액의 총 개수만큼 조합을 짜주는 라이브러리
for pos in combinations(culture_media, g+r):
    # pos : 배양액을 뿌릴 위치
    per(0, pos, g, r)



print(max_flower)
