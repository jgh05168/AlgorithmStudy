'''
항상 같은 색의 보석만 가져간다
질투심 = 가장 많은 보석의 개수
-> 질투심이 최소가 되게 하자

풀이:
못가져가는 애들도 있지만, 색은 같아야한다 ? -> 올림으로 가져가는 애들 수를 센다
만약 가져가는 애들 > 애들 수 : (mid + 1, end)
아니라면, : (start, mid)

start 출력
'''

import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
dia = [int(input()) for _ in range(m)]

start, end = 1, max(dia)

while start < end:
    mid = (start + end) // 2

    # 보석 가져가는 애들 계산해주기
    tmp_child = 0
    for jewel in dia:
        tmp_child += math.ceil(jewel / mid)

    if tmp_child > n:
        start = mid + 1
    else:
        end = mid

print(start)