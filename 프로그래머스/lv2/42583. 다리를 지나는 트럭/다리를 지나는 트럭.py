from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 1
    bridge = deque([0] * (bridge_length - 1))
    truck_weights = deque(truck_weights)
    sum_trucks = 0


    ## sum() 함수의 시간복잡도 : O(n)이기 때문에 매 반복문마다 사용하기에는 무리가 있음 
    # --> 다리 위의 트럭의 누적합, 다리를 통과하는 트럭들의 누적차를 변수로 지정
    while truck_weights:
        sum_trucks += truck_weights[0]
        if sum_trucks <= weight:
            bridge.append(truck_weights.popleft())
        else:
            sum_trucks -= truck_weights[0]
            bridge.append(0)
        sum_trucks -= bridge.popleft()
        time += 1

    return time + len(bridge)
