import sys
input = sys.stdin.readline

#     1   2   3  4   5  6  7  8
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

raindr = [1, 1, -1, -1]
raindc = [1, -1, -1, 1]


def moveCloud(case, time):
    for cloud in range(len(clouds)):
        # 범위를 벗어났을 경우 맨 뒤 혹은 맨 앞으로 인덱스를 이동
        row = (clouds[cloud][0] + dr[case - 1] * time) % N
        col = (clouds[cloud][1] + dc[case - 1] * time) % N

        # 각 구름의 좌표 업데이트
        clouds[cloud][0], clouds[cloud][1] = row, col
        # 구름의 위치이므로 visited를 True로 설정
        visited[row][col] = 1
        # 옮겨진 구름의 위치에 비가 1씩 내린다.
        grid[row][col] += 1


def increaseRain():
    for cloud in range(len(clouds)):
        cnt = 0
        row, col = clouds[cloud][0], clouds[cloud][1]
        # 대각선에 물이 차있는 바구니 개수 체크
        for d in range(len(raindr)):
            nrow, ncol = row + raindr[d], col + raindc[d]
            if 0 <= nrow < N and 0 <= ncol < N and grid[nrow][ncol]:
                cnt += 1

        # 차있는 개수만큼 물을 증가시켜준다.
        grid[row][col] += cnt


def makeCloud():
    new_clouds = []
    for row in range(N):
        for col in range(N):
            # 이전에 형성된 구름이 아니고, 물의 양이 2 이상인 경우
            if not visited[row][col] and grid[row][col] > 1:
                grid[row][col] -= 2             # 현재 물의 양 - 2
                new_clouds.append([row, col])   # 새로운 구름조각에 추가

    return new_clouds


# input
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

for _ in range(M):
    # 구름의 좌표들을 방문했다고 표시하기 위한 배열 생성
    visited = [[0] * N for _ in range(N)]
    di, si = map(int, input().split())

    # 구름을 움직이고, 비를 1씩 내리게 한다
    moveCloud(di, si)

    new_clouds = []
    # 구름의 대각선에 물이 있는지 확인하고 물의 구름의 물의 양을 증가시키는 함수
    increaseRain()

    # 새로운 구름 형성
    clouds = makeCloud()

# 모든 바구니에 담긴 물의 총 합
total = 0
for i in range(N):
    total += sum(grid[i])

print(total)


