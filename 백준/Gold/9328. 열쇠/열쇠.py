'''
기본적으로 갖고 있는 열쇠에 대한 2차원 visited 배열 생성
    - 열쇠를 하나씩 얻을 때마다 새로운 visited 배열을 append
바깥에 빈 배열 하나를 둘러준다.
열쇠 배열 하나 만들어주기
'''

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(srow, scol, v_idx):
    global doc_cnt
    queue = deque()
    visited.append([[0] * m for _ in range(n)])
    visited[v_idx][srow][scol] = 1
    queue.append((srow, scol))

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[v_idx][nrow][ncol] and building[nrow][ncol] != '*':
                # 열쇠 찾은 경우
                if building[nrow][ncol] == '$':
                    doc_cnt += 1
                    building[nrow][ncol] = '.'
                    queue.append((nrow, ncol))
                    visited[v_idx][nrow][ncol] = 1
                elif building[nrow][ncol].isalpha():
                    # 키 일 경우
                    if building[nrow][ncol].islower() and building[nrow][ncol] not in keys:
                        keys.add(building[nrow][ncol])
                        building[nrow][ncol] = '.'
                        bfs(0, 0, v_idx + 1)
                        return
                    # 문 일 경우
                    else:
                        # 만약 키가 존재한다면
                        if building[nrow][ncol].lower() in keys:
                            queue.append((nrow, ncol))
                            visited[v_idx][nrow][ncol] = 1
                else:
                    queue.append((nrow, ncol))
                    visited[v_idx][nrow][ncol] = 1


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    building = [['.'] * (m + 2)]
    for _ in range(n):
        building.append(['.'] + list(input().rstrip()) + ['.'])
    building.append(['.'] * (m + 2))
    n, m = len(building), len(building[0])
    keys = set(list(input().rstrip()))
    sangeun = (0, 0)
    visited = []
    doc_cnt = 0

    bfs(0, 0, 0)
    print(doc_cnt)
