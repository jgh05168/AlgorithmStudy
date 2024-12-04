'''
1. 2차원 좌표의 n개의 포인트 존재, 서로다른 번호를 갖는다.
2. 로봇마다 정해진 운송 경로가 존재. m개이며, 할당된 포인트 순서대로 방문
3. 사용되는 로봇은 x대, 0초에 동시 출발
4. 최단경로로 이동. 우선순위는 r이 변한 뒤, c가 변하는 이동 순서
5. 마지막 포인트에 도착한 로봇은 벗어난다.

현재 설정대로 로봇이 움직일 때 위험 상황이 총 몇 번 일어나는지 알고싶음
- 어떤 시간에 여러 좌표에서 위험 상황이 발생한다면 그 횟수를 모두 더함

풀이 : 좌표의 위치 초기화
2차원 grid
최단경로 생각해주기 : however, 장애물은 없기 때문에 맨해튼거리로 계산 가능
현재 로봇의 위치를 생각해주기 : 어디로 가야할 지 정보를 찾기
'''
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def solution(points, routes):
    answer = 0
    
    def get_distance(r1, c1, r2, c2):
        return abs(r1 - r2) + abs(c1 - c2)
    
    def move_robots(robots, routes):
        # 겹치는 위치 체크해야된다.
        new_robot_loc = []
        arrived_loc = set()
        collision = set()
        for robot in range(len(robots)):
            # 이미 종료한 로봇에 대한 처리
            if not robots[robot]:
                new_robot_loc.append(0)
                continue
            # 현재 위치에서 목적지까지 위치 먼저 계산
            r, c = robots[robot]
            dest = routes[robot][0]
            er, ec = points[dest]
            cur_dist = 10001
            # 새로운 위치 계산해보기
            new_r, new_c = r, c
            for d in range(len(dr)):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                    new_dist = get_distance(nr, nc, er, ec)
                    if new_dist < cur_dist:
                        new_r, new_c = nr, nc
                        cur_dist = new_dist
            # 현재 위치 일단 중복되는지 저장
            if (new_r, new_c) in arrived_loc:
                collision.add((new_r, new_c))
            else:
                arrived_loc.add((new_r, new_c))
            # 현재 위치가 목적지인지 확인
            if grid[new_r][new_c] == dest:
                routes[robot].popleft()
            # 종료되었다면, 빠져나가기
            if not routes[robot]:
                new_robot_loc.append(0)
            else:
                # 새로운 로봇 위치를 저장
                new_robot_loc.append((new_r, new_c))
        return new_robot_loc, routes, len(collision)
    
    
    n = 100
    grid = [[0] * (n) for _ in range(n)]
    points = [0] + points
    for i in range(1, len(points)):
        grid[points[i][0] - 1][points[i][1] - 1] = i
        points[i] = (points[i][0] - 1, points[i][1] - 1)
    # 로봇 정보 찾기
    cur_robots = [0]
    # 시작 위치부터 겹치는 경우도 생각해줘야한다.
    arrived_loc = set()
    collision = set()
    for i in range(len(routes)):
        routes[i] = deque(routes[i])
        cur_robots.append(points[routes[i].popleft()])
        if cur_robots[-1] in arrived_loc:
                collision.add(cur_robots[-1])
        else:
            arrived_loc.add(cur_robots[-1])
    answer += len(collision)
    
    robot_cnt = len(routes) + 1
    routes = [0] + routes
    # 로봇 움직이기 시작
    while True:
        # 1. 로봇 동시에 움직이기
        cur_robots, routes, collision = move_robots(cur_robots, routes)
        answer += collision
        # 2. 종료조건 확인
        if cur_robots.count(0) == robot_cnt:
            break
    return answer