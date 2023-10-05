'''
n * m 격자 미로가 주어진다.
x, y 에서 출발해 r, c로 이동해서 탈출해야한다.

조건
1. 격자 밖으로는 나갈 수 없다.
2. 이동하는 거리가 총 k여야 한다. 같은 격자를 2번 이상 방문해도 된다. -> visited를 안쓰고 ?
문자열이 사전 순으로 가장 빠른 경로로 탈출해야 한다.

l, r, u, d = 좌, 우, 상, 하

bfs -> 목적지에 횟수만큼 도달한 경우 문자열로 출력

- 문자열도 min, max 별로 비교할 수 있다.
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]
str_list = ['d', 'l', 'r', 'u']
answer = ''

def bfs(srow, scol, erow, ecol, k, n, m):
    global answer
    queue = deque()
    queue.append((srow, scol, '', 0))

    while queue:
        row, col, move_str, cnt = queue.popleft()

        if (row, col) == (erow, ecol) and cnt == k:
            answer = move_str
            break

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m:
                if abs(nrow - erow) + abs(ncol - ecol) + cnt + 1 > k:
                    continue
                queue.append((nrow, ncol, move_str + str_list[d], cnt + 1))
                break

def solution(n, m, x, y, r, c, k):
    global answer
    answer = ''

    bfs(x - 1, y - 1, r - 1, c - 1, k, n, m)
    if answer == '':
        return 'impossible'
    else:
        return answer

print(solution(3, 4, 2, 3, 3, 1, 5))