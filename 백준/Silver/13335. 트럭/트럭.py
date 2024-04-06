'''
트럭의 순서는 바꿀 수 없다 : sort x
트럭의 무게는 다르다
w대의 트럭만 동시에 올라갈 수 있다.
다리 위에 올라가있는 무게의 합은 다리의 최대 하중 L보다 작거나 같아야 한다.
다리 위에 완전히 올라가지 못한 트럭의 무게는 포함하지 않는다.

풀이 : 그냥 시뮬레이션, 덱에 넣은 뒤 다 돌려보기
'''

from collections import deque
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck_list = deque(list(map(int, input().split())))

on_bridge = [0] * w
min_time = 1
while True:
    # 다리 위 트럭 한 칸씩 땡겨주기 (0번 인덱스 트럭은 빠져나간다)
    for idx in range(1, len(on_bridge)):
        on_bridge[idx - 1] = on_bridge[idx]
    on_bridge[-1] = 0   # 마지막 위치 초기화
    # 다리에 올라갈 수 있는지 체크
    if truck_list and sum(on_bridge) + truck_list[0] <= l:
        on_bridge[-1] = truck_list.popleft()

    if not sum(on_bridge) and not truck_list:
        break
    else:
        min_time += 1

print(min_time)