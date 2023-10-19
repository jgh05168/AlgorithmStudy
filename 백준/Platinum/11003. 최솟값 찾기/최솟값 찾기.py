'''
i - L + 1이 처음값이 되는 경우 : i = L - 1

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
