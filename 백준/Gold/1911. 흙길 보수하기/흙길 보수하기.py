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
water_list.sort(key=lambda x: x[1])

idx = water_list[-1][1]
ans = 0
while water_list:
    start, end = water_list.pop()
    if idx > end:
        idx = end
    while idx > start:
        idx -= l
        ans += 1

print(ans)