'''
풀이:
1500 x 1500
2차원 for문이 가능할까 ? 가능하지

2중 for문 돌면서 heapq에 저장
n만큼 pop
======메모리 초과======

그냥 ans 배열 하나 만들어서 현재 값보다 큰 지, 작은 지 체크하자
'''

import sys, heapq
input = sys.stdin.readline

n = int(input())
pq = []
ans = []
for i in range(n):
    tmp = list(map(int, input().split()))

    # 한 번 tmp sort 한 다음, ans의 맨 앞 값보다 큰 값들만 heappush한다.
    # 이 때 제일 작은 값은 pop
    tmp.sort(reverse=True)
    if i == 0:
        for j in range(n):
            heapq.heappush(ans, tmp[j])
    else:
        for j in range(n):
            if tmp[j] > ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans, tmp[j])
            else:
                break

print(ans[0])