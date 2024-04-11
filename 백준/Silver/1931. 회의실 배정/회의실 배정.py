'''
회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대 개수 찾기

풀이:
1. 끝나는 시간이 빠른 순으로 정렬
2. 겹치는 시간이라면 pass
'''

import sys
input = sys.stdin.readline

n = int(input())
timetable = []
for _ in range(n):
    timetable.append(tuple(map(int, input().split())))

timetable.sort(key=lambda x: (x[1], x[0]))

cnt = 0
cur_end = 0
for start, end in timetable:
    if start < cur_end:
        continue
    else:
        cur_end = end
        cnt += 1

print(cnt)