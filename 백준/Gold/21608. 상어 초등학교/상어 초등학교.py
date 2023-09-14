'''
1. 초기 시작 위치 : 중앙 지점 중 왼쪽 위에 첫번째 학생을 놓고 시작한다

2. 다음 학생부터 입력을 받고, 좋아하는 학생이 자리에 앉아있는지 문제의 수식으로 탐색
    abs(r1 - r2) + abs(c1 - c2) = 1인 경우 인접하다고 한다.
    -> 그냥 상하좌우 방향벡터로 탐색해도 된다.
    2-1. 만약 좋아하는 학생이 자리에 앉았다면, 그 학생의 인접한 칸 개수를 센다
    2-2. 좋아하는 학생이 자리에 없다면, 자리를 다시 순차적으로 돌아보면서 인접한 칸 중 빈 칸이 가장 많은 곳에 앉는다.

3. 인접한 칸 개수가 최대인 것들의 배열을 만들어 준 다음 (row, col) 기준으로 오름차순 정렬

4. 모든 조건이 맞지 않다면 3번의 배열에서 맨 첫번째 위치에 학생을 앉힌다.

5. 1 ~ 4과정이 끝났으면 모든 학생들을 순회하며 만족도조사 진행
    5-1. 4방면에 대해서 모두 조사
'''

import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
classroom = [[0] * N for _ in range(N)]
seat_list = [0] * (N ** 2 + 1)    # visited
all_like_stds = [0] * (N ** 2 + 1)

# grid idx는 [0, 0]부터 시작. 학생정보 idx는 1부터 시작
for time in range(N ** 2):
    cur_student, *like_students = list(map(int, input().split()))
    all_like_stds[cur_student] = like_students
    if not time:
        classroom[1][1] = cur_student
        seat_list[cur_student] = (1, 1)
    else:
        # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
        max_adj_1 = 0
        can_seat_list = []
        for i in range(N):
            for j in range(N):
                if not classroom[i][j]:
                    cnt_adj_1 = 0
                    for d in range(len(dr)):
                        ni, nj = i + dr[d], j + dc[d]
                        if 0 <= ni < N and 0 <= nj < N and classroom[ni][nj] in like_students:      # 좋아하는 학생이 많은 경우를 확인하자
                            cnt_adj_1 += 1
                    # 만약 인접한 칸의 개수가 max 보다 크다면
                    if max_adj_1 < cnt_adj_1:
                        max_adj_1 = cnt_adj_1
                        can_seat_list.clear()
                        can_seat_list.append((i, j))
                    # 만약 인접한 칸의 개수가 max 와 동일하다면
                    elif max_adj_1 == cnt_adj_1:
                        can_seat_list.append((i, j))

        # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
        if len(can_seat_list) == 1:
            row, col = can_seat_list.pop()
            classroom[row][col] = cur_student
            seat_list[cur_student] = (row, col)
            continue
        else:
            max_adj_list = []
            max_cnt = 0
            for row, col in can_seat_list:
                cnt = 0
                for d in range(len(dr)):        # 인접한 자리들 탐색
                    nrow, ncol = row + dr[d], col + dc[d]
                    # 자리가 비어있다면
                    if 0 <= nrow < N and 0 <= ncol < N and not classroom[nrow][ncol]:
                        cnt += 1
                # 만약 인접한 칸의 개수가 max 보다 크다면
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_adj_list.clear()
                    max_adj_list.append((row, col))
                # 만약 인접한 칸의 개수가 max 와 동일하다면
                elif max_cnt == cnt:
                    max_adj_list.append((row, col))

        # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        if len(max_adj_list) == 1:
            row, col = max_adj_list.pop()
            classroom[row][col] = cur_student
            seat_list[cur_student] = (row, col)
            continue
        else:
            max_adj_list.sort(key=lambda x: (x[0], x[1]))
            row, col = max_adj_list.pop(0)
            classroom[row][col] = cur_student
            seat_list[cur_student] = (row, col)

# 만족도조사
satisfied_score = 0
for row in range(N):
    for col in range(N):
        satisfied_cnt = 0
        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < N and 0 <= ncol < N and (classroom[nrow][ncol] in all_like_stds[classroom[row][col]]):
                satisfied_cnt += 1
        if satisfied_cnt == 2:
            satisfied_score += 10
        elif satisfied_cnt == 3:
            satisfied_score += 100
        elif satisfied_cnt == 4:
            satisfied_score += 1000
        else:
            satisfied_score += satisfied_cnt

print(satisfied_score)
