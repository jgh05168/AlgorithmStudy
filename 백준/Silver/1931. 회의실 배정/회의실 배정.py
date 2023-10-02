'''
그리디
시작시간(두번째 조건)과 끝나는 시간(첫번째 조건)이 가장 빠른 순으로 정렬한 뒤 시작 시간과 비교하여 계산한다.
'''

import sys
input = sys.stdin.readline

schedules = []
N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    schedules.append((start, end))

schedules.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간대, 시작 시간대 순으로 정렬

cnt = 0
endtime = 0
for i in range(len(schedules)):
    starttime, nend = schedules[i]
    if starttime < endtime:
        continue
    cnt += 1
    endtime = nend

print(cnt)

