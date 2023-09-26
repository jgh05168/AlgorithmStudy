'''
우선 정렬을 한다

이후 처음부터 개수만큼 묶어서 진행해보기(순열처럼)
'''

from collections import deque
N, M = map(int, input().split())
locs = list(map(int, input().split()))

plus = []
minus = []
for i in locs:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)

minus.sort()
plus.sort()


way = 0
start, end = 0, len(plus) - 1

# 음수 더하기
while start + M < len(minus):
    way += abs(minus[start]) * 2
    start += M
# 양수 더하기
while end - M > -1:
    way += plus[end] * 2
    end -= M

if start < len(minus) and end >= 0:
    way += (plus[end] + abs(minus[start])) * 2
elif start < len(minus) and end < 0:
    way += abs(minus[start]) * 2
else:
    way += plus[end] * 2

if not len(minus):
    way -= plus[-1]
elif not len(plus):
    way -= abs(minus[0])
elif len(minus) and len(plus):
    if abs(minus[0]) < plus[-1]:
        way -= plus[-1]
    else:
        way -= abs(minus[0])
else:
    way = 0
print(way)