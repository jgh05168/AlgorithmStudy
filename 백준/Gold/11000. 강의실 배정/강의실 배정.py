'''
강의실 배정

1. 우선순위 큐에 (강의 시간, start, end) 형식으로 삽입
2. 하나씩 꺼내보며 강의를 배정한다.
'''

import sys, heapq
input = sys.stdin.readline

n = int(input())
pq = []
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(pq, (s, e))       # 수업이 짧은 순으로 우선순위에 저장

timetable = []        # 강의실 배정 시간표
while pq:
    start, end = heapq.heappop(pq)
    # 만약 시간표가 비었거나 가장 작은 시간표의 end보다 start가 더 빠르다면 그냥 새로운 강의실 지정
    if not timetable or timetable[0][0] > start:
        heapq.heappush(timetable, (end, start))
    else:       # 아니라면 현재 강의실은 이미 처리했으니 빼준 뒤 새로운 강의실로 배정
        heapq.heappop(timetable)
        heapq.heappush(timetable, (end, start))

print(len(timetable))