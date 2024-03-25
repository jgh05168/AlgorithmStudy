'''
도시들은 일직선 상에 있음

기름통 : 무제한
1km에 1L
각 도시에는 단 하나의 주유소만 존재. 주유소의 리터당 가격은 다를 수 있음
최소비용찾기

풀이:
1. 기름값 0원이라 하고 시작
2. 도시를 하나씩 이동할수록 (기름값이 가장 작은 곳 * 도로의 길이)를 더해준다.
'''

import sys
input = sys.stdin.readline

n = int(input())
roads = [0] + list(map(int, input().split()))
cities = list(map(int, input().split()))

min_v = 0
min_cost = cities[0]
for i in range(1, n):
    if cities[i - 1] < min_cost:
        min_cost = cities[i - 1]
    min_v += min_cost * roads[i]
print(min_v)