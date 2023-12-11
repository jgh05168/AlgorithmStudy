'''
heapq 사용 : 이동 칸 개수, 행, 열

1. 최단경로로 이동하여 승객 찾기
2. 승객을 찾으면 목적지로 데려다주기 + 소모 연료 체크

- 승객을 태우거나, 목적지까지 도달했을 경우 좌표 초기화
- 승객은 key(alphabet), 승객의 도착지는 마이너스로 표시하여 딕셔너리에 따로 저장해주기
'''

from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def taxi_to_passenger(srow, scol):      # 여기서는 다익스트라를 사용할 필요 x
    global fuel
    pq = []
    heapq.heappush(pq, (0, srow, scol))
    visited = [[0] * n for _ in range(n)]
    visited[srow][scol] = 1
    passenger = 0

    while pq:
        move, row, col = heapq.heappop(pq)


        # 현재 위치가 승객인지 확인
        if taxi_map[row][col] != '0' or taxi_map[row][col] != '1':
            if passenger_info[taxi_map[row][col]]:
                passenger = taxi_map[row][col]
                fuel -= move
                return True, row, col, passenger

        # 연료를 다 썼는지 확인
        if fuel - move <= 0:
            return False, -1, -1, -1

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol] and taxi_map[nrow][ncol] != '1':
                heapq.heappush(pq, (move + 1, nrow, ncol))
                visited[nrow][ncol] = 1

    return False, -1, -1, -1


def passenger_move(srow, scol, passenger):
    global fuel
    pq = []
    heapq.heappush(pq, (0, srow, scol))
    visited = [[0] * n for _ in range(n)]
    visited[srow][scol] = 1

    if (srow, scol) == passenger_info[passenger]:
        return True, srow, scol

    while pq:
        move, row, col = heapq.heappop(pq)

        # 연료를 다 썼는지 확인
        if fuel - move <= 0:
            return False, -1, -1

        for d in range(len(dr)):
            nrow, ncol = row + dr[d], col + dc[d]
            if 0 <= nrow < n and 0 <= ncol < n and not visited[nrow][ncol] and taxi_map[nrow][ncol] != '1':
                if (nrow, ncol) == passenger_info[passenger]:
                    fuel += (move + 1)
                    passenger_info[passenger] = 0
                    return True, nrow, ncol
                heapq.heappush(pq, (move + 1, nrow, ncol))
                visited[nrow][ncol] = 1

    return False, -1, -1


n, m, fuel = map(int, input().split())
taxi_map = [list(input().split()) for _ in range(n)]
trow, tcol = map(int, input().split())
trow -= 1
tcol -= 1
passenger_info = defaultdict(tuple)
for i in range(m):
    sr, sc, er, ec = map(int, input().split())
    taxi_map[sr - 1][sc - 1] = chr(ord('a') + i)
    passenger_info[chr(ord('a') + i)] = (er - 1, ec - 1)

check_move = True
spend_fuel = 0
# 택시의 이동이 멈출 때까지 반복
while m:
    check_move, trow, tcol, passenger_name = taxi_to_passenger(trow, tcol)

    if not check_move:
        print(-1)
        exit()

    # 승객의 위치를 찾았으니 목적지까지 이동
    check_move, trow, tcol = passenger_move(trow, tcol, passenger_name)

    if not check_move:
        print(-1)
        exit()

    m -= 1

print(fuel)