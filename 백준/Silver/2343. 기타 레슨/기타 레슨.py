'''
블루레이의 크기를 기준으로 이분탐색 진행
초기 start = 0, end = sum()
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

start, end = 0, max(lessons) * N
min_size = sum(lessons)
while start <= end:
    mid = (start + end) // 2

    size = 0
    cnt = 1
    for lesson in lessons:
        if size + lesson > mid:
            cnt += 1
            size = lesson
            if size > mid:          # 현재 들어온 값이 mid보다 크다면 애초에 mid 블루레이 크기는 사용불가능함
                start = mid + 1
                break
        else:
            size += lesson
    else:
        if cnt <= M:       # 블루레이 개수가 더 작을 경우, 들어갈 수 있는 강의 크기를 줄여야 한다.
            end = mid - 1
            min_size = min(min_size, mid)
        else:
            start = mid + 1

print(min_size)

