'''
완전 탐색

1 ~ N - 1의 지점을 탐색한다.
백트래킹으로 탐색하여 가능한 부분은 visited 배열에 1로 표시
다섯 구간 모두 탐색을 진행한 후 겹치는 부분이 없다면 넘어가는 방식으로 하자

3 * 10 * 10 * 5
'''

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def recur(flower, cost):
    global min_cost
    if flower == 3:
        if min_cost > cost:
            min_cost = cost
        return

    leaf_list = []
    for row in range(1, N - 1):
        for col in range(1, N - 1):
            if not visited[row][col]:
                temp = ground[row][col]
                visited[row][col] = 1
                leaf_list.append((row, col))
                for d in range(len(dr)):
                    nrow, ncol = row + dr[d], col + dc[d]
                    if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol]:
                        temp += ground[nrow][ncol]
                        visited[nrow][ncol] = 1
                        leaf_list.append((nrow, ncol))
                    else:
                        break
                else:
                    recur(flower + 1, cost + temp)
            for lrow, lcol in leaf_list:
                visited[lrow][lcol] = 0

    return


N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
min_cost = int(1e9)

recur(0, 0)
print(min_cost)