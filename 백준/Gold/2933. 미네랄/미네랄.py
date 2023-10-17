'''
구현, bfs, 탐색
굳이 배열생성하여 count 해 줄 필요는 없을듯 ? -> 내려갈 수 있다면 초기화 후 이동하기
던지는 사람에 따라서 탐색 col을 정해줘야한다.
층 별 탐색은 무조건 row 역 순

'''

from collections import deque
import sys, copy
input = sys.stdin.readline


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol, color):
    global clusters
    queue = deque()
    queue.append((srow, scol))
    minerals[srow][scol] = color
    if color > 1:
        clusters.append((srow, scol))

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            # 범위 안에 있고, 방문하지 않았고, 미네랄이라면 큐에 저장(graph)
            if 0 <= nrow < R and 0 <= ncol < C and not minerals[nrow][ncol] and cave[nrow][ncol] == 'x':
                minerals[nrow][ncol] = color
                queue.append((nrow, ncol))
                if color > 1:
                    clusters.append((nrow, ncol))


def move_down(clusters, length):
    for row, col in clusters:
        cave[row][col] = '.'
        cave[row + length][col] = 'x'




R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
throws = list(map(int, input().split()))

for throw in range(N):
    crash = False
    if throw % 2:       # 상근 : col 오른쪽부터 탐색
        attack_row = R - throws[throw]      # 어느 층에 막대를 던질 것인지
        # 미네랄 부수기
        for attack_col in range(C - 1, -1, -1):
            if cave[attack_row][attack_col] == 'x':
                cave[attack_row][attack_col] = '.'      # 미네랄 존재한다면 부수기 성공!
                crash = True
                break
    else:               # 창영 : col 왼쪽부터 탐색
        attack_row = R - throws[throw]      # 어느 층에 막대를 던질 것인지
        # 미네랄 부수기
        for attack_col in range(C):
            if cave[attack_row][attack_col] == 'x':
                cave[attack_row][attack_col] = '.'      # 미네랄 존재한다면 부수기 성공!
                crash = True
                break

    if crash:       # 미네랄 부쉈다면 탐색 시작
        # 클러스터 덩어리가 부숴졌는지 확인만 해보자.
        # 아래부터 탐색
        minerals = [[0] * C for _ in range(R)]
        color = 1
        clusters = []
        for height in range(R - 1, -1, -1):
            for width in range(C):
                if height == R - 1:  # 바닥에 붙어있는 경우는 1로 취급
                    color = 1  # 어차피 바닥부터 탐색하기때문에 1로 값설정해줘도 괜찮다.
                else:
                    color = 2
                if not minerals[height][width] and cave[height][width] == 'x':
                    bfs(height, width, color)

        clusters.sort(key=lambda x: x[0], reverse=True)
        # 만약 두덩이로 나뉘어졌다면
        if color > 1:
            # 각 col 별 땅(클러스터)와 다른 클러스터 거리 최솟값을 찾은뒤 그만큼 내려가기
            length = 100
            for cluster_row, cluster_col in clusters:
                # 거리재보기 위해 땅/기본클러스터 최대위치 확인
                temp_length = 0
                base_height = R - 1
                while base_height > cluster_row:
                    if cave[base_height][cluster_col] == '.' or minerals[base_height][cluster_col] == minerals[cluster_row][cluster_col]:
                        temp_length += 1
                    else:
                        temp_length = 0
                    base_height -= 1

                length = min(length, temp_length)

            move_down(clusters, length)


for h in range(R):
    print(''.join(cave[h]))



