'''
격자, 데이터값이 부여된다.

백신을 놓으면 격자의 칸 중 하나에 항체 생성
현재 속해 있는 칸과 같은 데이터 값을 가지면서 상하좌우로 인접한 칸이 있는 경우 퍼져나간다.
-> 다 퍼진다면 모두 동일한 값으로 새로 업데이트된다. (값이 같을 수도 있음)


풀이 :
1. 백신 맞기 이전과 결과를 비교한다
2. 만약 값이 다르다면 bfs 진행하여 인접한 백신 맞기 전을 결과값으로 다 바꿔준다
- 그런 다음 나머지 배열이 같다면 YES 출력, 또 다른 부분이 존재한다면 NO 출력
'''

from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(srow, scol, bval, aval):
    visited = [[0] * m for _ in range(n)]
    visited[srow][scol] = 1
    queue = deque([(srow, scol)])
    before[srow][scol] = aval

    while queue:
        row, col = queue.popleft()

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and before[nrow][ncol] == bval:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = 1
                before[nrow][ncol] = aval
                if before[nrow][ncol] != after[nrow][ncol]:
                    print("NO")
                    exit()


n, m = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]

flag = 0
# 같은지 비교
for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            if not flag:
                bfs(i, j, before[i][j], after[i][j])
                flag = 1
            else:
                print("NO")
                exit()

print("YES")