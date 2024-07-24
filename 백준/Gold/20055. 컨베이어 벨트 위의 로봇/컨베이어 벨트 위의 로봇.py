'''
컨베이어벨트 위 로봇

로봇이 내리는 위치에 도달하면 그 즉시 내린다.
로봇을 올리는 위치에 올리거나, 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 감소한다.

1. 벨트가 한 칸 회전
2. 가장 먼저 벨트에 올라간 로봇부터, 회전하는 방향으로 이동.
    - 이동할 수 없다면 가만히 있기
3. 올리는 위치 내구도가 0이 아니라면 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 k개 이상이라면 과정 종료

풀이 :
1차원 리스트로 생각하고 deque로 풀기
로봇의 위치 배열도 갖고 있기. (배열 돌릴 떄 같이 처리해주어야 함)

---- 배운점 ----
불필요한 조건을 추가하는 것보다, 같은 시간복잡도라면
나중에 한번에 처리해 주는 것이 더 효율적이다.
'''

from collections import deque
import sys
input = sys.stdin.readline


def rotate():
    # 우선 다 돌리기
    belt.rotate(1)
    robot.rotate(1)
    # 만약 로봇 내리는 곳에 로봇이 존재한다면, 내리기
    robot[n - 1] = 0


def move_robots():
    for i in range(n - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            belt[i + 1] -= 1
    robot[-1] = 0


def robot_setting():
    if not robot[0] and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1


n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)

ans = 0
while True:
    # 1. 벨트 한 칸씩 회전
    rotate()
    # 2. 로봇 이동시키기
    move_robots()
    # 3. 로봇 하나씩 올리기
    robot_setting()

    ans += 1
    # 내구성 체크(종료 조건)
    if belt.count(0) >= k:
        break

print(ans)