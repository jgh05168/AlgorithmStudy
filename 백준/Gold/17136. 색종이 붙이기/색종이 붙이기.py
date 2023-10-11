'''
정사각형 모양을 한 다섯 종류의 색종이가 있다.
-> length를 점점 늘려가며 탐색해보기

덮는 최소값 -> 색종이끼리도 덮히면 안된다.

- visited 배열 사용

백트래킹

200 * 5 * 5 * 5
'''

import sys
input = sys.stdin.readline


def dfs(cnt, used_papers):
    global min_v

    # val이 min_v보다 클 경우 반환
    if min_v <= used_papers:
        return

    # 종료 조건 : 모두 탐색되었을 때(visited의 1 개수 == 전체 1의 개수
    if cnt == ones:
        min_v = min(min_v, used_papers)
        return

    for srow, scol in color_list:
        if not visited[srow][scol]:
            for d in range(1, 6):
                if not paper_dict[d]:
                    continue

                temp = 0
                temp_list = []
                check = True
                for row in range(srow, srow + d):
                    for col in range(scol, scol + d):
                        if 0 <= row < n and 0 <= col < n and not visited[row][col] and paper[row][col]:
                            visited[row][col] = 1
                            temp += 1
                            temp_list.append((row, col))
                        else:
                            check = False
                            break
                    if not check:
                        break
                else:
                    paper_dict[d] -= 1
                    dfs(cnt + temp, used_papers + 1)

                while temp_list:
                    drow, dcol = temp_list.pop()
                    visited[drow][dcol] = 0
                if check:
                    paper_dict[d] += 1

            return

n = 10
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
paper_dict = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}

# 1인 부분 먼저 찾기
min_v = int(1e9)         # 최소값
ones = 0          # 1인 부분 개수
color_list = []
for i in range(n):
    for j in range(n):
        if paper[i][j]:
            color_list.append((i, j))
            ones += 1

if not ones:
    print(0)
else:
    dfs(0, 0)
    if min_v == int(1e9):
        print(-1)
    else:
        print(min_v)
