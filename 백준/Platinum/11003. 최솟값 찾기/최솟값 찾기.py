'''
우선순위 큐 사용

1. 우선순위 큐에 현재 인덱스의 값과 인덱스 번호를 튜플로 저장
2. 이후 heapq.heappop()을 통해 값을 뺀 뒤 최솟값의 인덱스가 현재 범위를 만족하는지 확인
    2-1. 만약 만족하지 않는다면 2번과정에서 인덱스 범위를 만족할 때까지 반복
3. 범위를 만족하였다면 최솟값 출력 후 다시 heapq.heappush()
4. 2 ~ 3 과정 반복

L - 1보다 작은지, 큰 지 범위를 나누어서 해보기
'''

from collections import deque
import sys, heapq
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

D = []
# 값은 L만큼 존재한다.
# 처음부터 값을 큐에 넣은 뒤 출력하는 방식

for i in range(N):
    heapq.heappush(D, (A[i], i))
    ans = heapq.heappop(D)
    if i - L + 1 <= ans[1] <= i:
        print(ans[0], end=' ')
        heapq.heappush(D, ans)
    else:
        get_val = False
        while not get_val:
            ans = heapq.heappop(D)
            if i - L + 1 <= ans[1] <= i:
                print(ans[0], end=' ')
                heapq.heappush(D, ans)
                get_val = True

# '''
# deque 사용.
# '''
# from collections import deque
# import sys
# input = sys.stdin.readline

# N, L = map(int, input().split())
# li = list(map(int, input().split()))
# q = deque()
# for i in range(N):
#     while q and q[-1] > li[i]:      # 큐에 값이 존재하고, 큐의 마지막값이 현재 들어온 값보다 큰 경우 뒤에서부터 pop
#         q.pop()                     # = 현재 값보다 큰 이전 값들은 더이상 필요가 없다.
#     q.append(li[i])         # 현재 값 append

#     # 만약 i가 L 보다 크고 범위의 가장 낮은 값이 q의 첫번째 값이라면, 하나 꺼내기.
#     if i >= L and li[i - L] == q[0]:
#         q.popleft()

#     print(q[0], end=' ')
