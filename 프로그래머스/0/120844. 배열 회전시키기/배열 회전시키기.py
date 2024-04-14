from collections import deque
import sys
input = sys.stdin.readline


def solution(numbers, direction):
    deq_numbers = deque(numbers)
    
    if direction == "right":
        deq_numbers.appendleft(deq_numbers.pop())
    else:
        deq_numbers.append(deq_numbers.popleft())
    answer = list(deq_numbers)
    return answer

