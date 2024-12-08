'''
각 큐의 원소 합이 같도록 만들려고 한다.
이 때, 필요한 작업의 최소 횟수를 구하고자 함

몬만드는 조건 1. 두 큐의 합이 홀수인 경우
몬만드는 조건 2. 두 큐 중 하나가 비게 되는 경우
몬만드는 조건 3. 맨 처음 녀석이 두 번 popleft 되는 경우

이 조건을 만족하지 않는다면, 그냥 큐에서 하나씩 빼본 뒤, 비교하기

'''

from collections import deque

def solution(queue1, queue2):
    answer = 0
    total1, total2 = sum(queue1), sum(queue2)
    # 종료조건 1
    if (total1 + total2) % 2:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    for _ in range(1000000):
        if total1 == total2:
            break
        elif total1 < total2:
            queue1.append(queue2.popleft())
            answer += 1
            if not queue2:
                return -1
            total1 += queue1[-1]
            total2 -= queue1[-1]
        else:
            queue2.append(queue1.popleft())
            answer += 1
            if not queue1:
                return -1
            total1 -= queue2[-1]
            total2 += queue2[-1]
    else:
        return -1    
    
    return answer

