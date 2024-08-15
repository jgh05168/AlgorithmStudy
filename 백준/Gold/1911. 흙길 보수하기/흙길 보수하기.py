'''
O(n)

풀이 :
웅덩이 리스트를 작성해서 for문 돌리면 무조건 시초난다.
-> 길이 l인 널빤지

뒤에서부터 막기
만약 막을 수 있다면 다 막고, 끝나는 지점 업데이트(막힌 부분보다 마지막 지점이 작다면, 출발지 변경)
만약 막을 수 없다면, 하나 더 추가하기
'''

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
water_list = [tuple(map(int, input().split())) for _ in range(n)]


ans = 0
#### 첫번째 방법(시간 오래 걸림)
# water_list.sort(key=lambda x: x[0])
# idx = water_list[-1][1]
# while water_list:
#     start, end = water_list.pop()
#     if idx > end:
#         idx = end
#     while idx > start:
#         idx -= l
#         ans += 1

#### 두번째 방법 : 두번째 while 문을 수학적으로 풀이
water_list.sort(key=lambda x: x[0], reverse=True)
idx = water_list[-1][0]
while water_list:
    start, end = water_list.pop()
    if idx < start:
        idx = start
    # 거리 계산
    diff = end - idx
    # 다 막혀 떨어질 때 vs 안막힐 때 차이 비교
    if not diff % l:
        ans += diff // l
        idx = end
    else:
        ans += diff // l + 1    # 무조건 막아야하므로 안막힌 부분을 덮기 위한 + 1
        # 다 덮었다는 가정 하에 시작 위치 업데이트
        idx = end + (l - diff % l)

print(ans)
