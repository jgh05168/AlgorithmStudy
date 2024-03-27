'''
A는 B를 먹는다
A는 자기보다 작은 먹이만 먹을 수 있다.

풀이:
for문 돌면서 이분탐색 진행
만약 자신보다 작은 값이 존재한다면, 바로 개수 세고 이분탐색 종료

'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    b_list.sort()

    cnt = 0
    for a in a_list:
        start, end = 0, m
        while start < end:
            mid = (start + end) // 2
            if a > b_list[mid]:
                start = mid + 1
            else:
                end = mid
        cnt += start      # 나보다 작은 위치까지의 개수들을 모두 더해준다.

    print(cnt)