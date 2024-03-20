'''
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

어떤 한 문서가 몇 번째로 인쇄되는지 알아내기

풀이 :
그냥 max(queue) 비교해서 가장 큰 값이면 pop, 아니면 다시 넣어주기
'''

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    result = 1
    while queue:
        if queue[0] < max(queue):
            queue.append(queue.popleft())

        else:
            if m == 0:
                break

            queue.popleft()
            result += 1

        # m 업데이트 필요
        if m > 0:
            m -= 1
        else:
            m = len(queue) - 1

    print(result)
