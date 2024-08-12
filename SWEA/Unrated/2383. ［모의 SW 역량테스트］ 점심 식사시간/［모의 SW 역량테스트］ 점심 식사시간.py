'''
n x n

최대한 빠른 시간 내에 내려가자

1. 계단 입구까지 이동시간 : 절댓값 맨해튼거리
2. 계단 내려가기
    - 계단 입구에 도착하면 1분 뒤 아래로 내려갈 수 있다.
    - 최대 3명까지만 올라갈 수 있다.
    - 3명이 계단을 내려가는 경우, 그 중 한 병이 계단을 완전히 내려갈 때 까지 입구에서 대기 = 자리에 가만히 있기
    - 계단마다 길이 k가 주어짐.
        - 계단에 올라가면 완전히 내려가는데 k분이 걸린다.

모든 사람이 계단을 내려가는 최소 시간을 찾기

풀이:
계단의 입구 : 2개
1. 모든 사람마다 어느 계단을 가는지 조합을 짠다.
2. 이동해보기 (bfs)
- 먼저 계단에 있는 사람부터 내려가기
- 이후 아직 층에 있는 사람들 한 칸 씩 이동
3. 최솟값 업데이트 -> 백트래킹 걸기
- 계단 각각에 list 설정 ((사람 번호, 계단 내려간 횟수))
- 도착했을 때 계단을 내려가는 사람의 수 cnt 후 내려갈 지 말 지 정하기

문제 자체가 도착하면 대기 -> k 번 만큼 내려감 -> 내려가서 빠져나오면 바로 새로운 대기하던 사람이 들어온다
==> 문제 조건을 잘 이해해야 함
'''

import heapq
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def move_people(select_door):
    # 1. 사람들 계단으로 이동
    global min_time
    visited = [[[0] * n for _ in range(n)] for _ in range(len(people))]
    queue = deque()
    for idx in range(len(people)):
        queue.append((people[idx][0], people[idx][1], idx, select_door[idx]))
        visited[idx][people[idx][0]][people[idx][1]] = 1

    # 계단 내려가는 큐도 있어야함
    stair1, stair2 = deque(), deque()
    wait1, wait2 = deque(), deque()
    tmp_time, end_person = 0, 0
    arrive_person = [0] * len(people)
    while True:
        # 종료 조건
        if tmp_time > min_time:
            return
        if end_person == len(people):
            break

        new_queue = deque()
        new_stair1, new_stair2 = deque(), deque()
        # 한 명 씩 이동했다면, 계단 내려가기

        if stair1:
            while stair1:
                move_cnt = stair1.popleft()
                move_cnt -= 1
                if move_cnt > 0:
                    new_stair1.append(move_cnt)
                else:
                    end_person += 1

        if stair2:
            while stair2:
                move_cnt = stair2.popleft()
                move_cnt -= 1
                if move_cnt > 0:
                    new_stair2.append(move_cnt)
                else:
                    end_person += 1

        while queue:
            r, c, person, door_num = queue.popleft()
            er, ec = doors[door_num]

            for d in range(len(dr)):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < n and 0 <= nc < n and not visited[person][nr][nc] and not arrive_person[person]:
                    if (nr, nc) == (er, ec):
                        arrive_person[person] = 1
                        # 문이 1번인지 2번인지 체크
                        if not door_num:
                            if len(stair1) + len(new_stair1) < 3:
                                new_stair1.append((grid[er][ec] + 1))
                            else:
                                wait1.append((grid[er][ec]))
                        else:
                            if len(stair2) + len(new_stair2) < 3:
                                new_stair2.append((grid[er][ec] + 1))
                            else:
                                wait2.append((grid[er][ec]))
                    else:
                        visited[person][nr][nc] = 1
                        new_queue.append((nr, nc, person, door_num))

        # 다 내려간 계단이 있는지 확인
        if len(new_stair1) < 3 and wait1:
            while len(new_stair1) < 3 and wait1:
                new_stair1.append(wait1.popleft())
        if len(new_stair2) < 3 and wait2:
            while len(new_stair2) < 3 and wait2:
                new_stair2.append(wait2.popleft())

        # 업데이트
        stair1, stair2 = new_stair1, new_stair2

        # 종료 조건
        tmp_time += 1
        queue = new_queue


    min_time = min(min_time, tmp_time)


def dfs(select_cnt, ppl_list):
    if select_cnt == len(people):
        move_people(ppl_list)

    else:
        for i in range(2):
            dfs(select_cnt + 1, ppl_list + [i])

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    people = []     # 사람은 인덱스로 번호 확인하기
    doors = []
    p_idx = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                people.append((i, j, p_idx))
                p_idx += 1
            elif grid[i][j] > 1:
                doors.append((i, j))

    min_time = int(1e9)
    dfs(0, [])


    print(f'#{tc} {min_time}')
