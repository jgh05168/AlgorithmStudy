# 이분탐색으로 조져보면 될 것 같은데 ..?
# 리프노드가 아닌 이상 무조건 1이여야 한다.

from collections import deque

def find_len(dummy_data, num):
    N = 0
    while True:
        if 2**N <= len(num) < 2**(N + 1):
            while len(num) < 2**(N + 1) - 1:
                num = '0' + num
                dummy_data.appendleft(1)
            break
        N += 1

    return num, dummy_data

def binary_search(num, dummy, start, end):
    if start >= end:
        return 1
    mid = (start + end) // 2
    # 부모가 더미노드 일 때 자식 노드에 1이 있으면 안된다.
    if not int(num[mid]):
        if int(num[(start + mid - 1) // 2]) or int(num[(mid + 1 + end) // 2]):
            return 0
    left = binary_search(num, dummy, start, mid - 1)
    if not left:
        return 0
    right = binary_search(num, dummy, mid + 1, end)
    if not right:
        return 0
    return 1


def solution(numbers):
    answer = []

    for num in numbers:
        s = bin(num)[2:]
        dummy_data = deque([0] * len(s))
        s, dummy_data = find_len(dummy_data, s)
        if len(s) == 1 and not int(s):
            answer.append(0)
        else:
            answer.append(binary_search(s, dummy_data, 0, len(s) - 1))
    return answer