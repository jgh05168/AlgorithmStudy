'''
주난이부터 시작해서 bfs 돌린 뒤 만나는 벽을 부순다
벽을 만난 파동에 대해서 체크해주기
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol):
    queue = deque()
    queue.append((srow, scol))
    visited = [[0] * m for _ in range(n)]
    visited[srow][scol] = 1
    break_students = set()

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and (nrow, ncol) not in break_students:
                if classroom[nrow][ncol] == '#':
                    return True
                elif classroom[nrow][ncol] == '1':
                    break_students.add((nrow, ncol))
                    classroom[nrow][ncol] = '0'
                else:
                    visited[nrow][ncol] = 1
                    queue.append((nrow, ncol))
    return False


n, m = map(int, input().split())
srow, scol, erow, ecol = map(int, input().split())
classroom = [list(input().rstrip()) for _ in range(n)]

cnt = 1
find = False
while True:
    find = bfs(srow - 1, scol - 1)

    if find:
        break
    cnt += 1

print(cnt)
