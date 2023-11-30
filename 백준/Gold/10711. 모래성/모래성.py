'''
완탐으로 풀면 시간초과
1000 x 1000

-> 파도의 위치를 큐에 저장 후 모래성을 마주할 때마다 -1을 해준다.
만약 마주한 곳이 0이라면 '.'으로 바꿔준 뒤 그 자리를 큐에 저장.

이 때 큐에는 몇 번의 파도인지 정보도 같이 저장해 주어야 한다.
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def bfs(waves):
    queue = waves
    wave_cnt = 0

    while queue:
        row, col, tmp_wave_cnt = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < h and 0 <= ncol < w and beach[nrow][ncol] != '.':
                beach[nrow][ncol] -= 1
                if not beach[nrow][ncol]:
                    queue.append((nrow, ncol, tmp_wave_cnt + 1))
                    beach[nrow][ncol] = '.'
                    if wave_cnt < tmp_wave_cnt + 1:
                        wave_cnt = tmp_wave_cnt + 1

    return wave_cnt


h, w = map(int, input().split())
beach = [list(input().rstrip()) for _ in range(h)]

# 파도 세기
waves = deque()
for i in range(h):
    for j in range(w):
        if beach[i][j] == '.':
            waves.append((i, j, 0))
        else:
            beach[i][j] = int(beach[i][j])

print(bfs(waves))