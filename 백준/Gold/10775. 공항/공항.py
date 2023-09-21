'''
union-find

1. 만약 도킹한 gate가 자기 자신이라면
    - 자신의 이전 gate를 부모로 묶어준 뒤 count + 1
2. 만약 부모의 값이 0(도킹할 수 없는 경우)일 경우 반복문을 빠져나온다.

ex)
input : 4
arrival_info = [0, 1, 2, 3, 3]

input : 1
arrival_info = [0, 0, 2, 3, 3]

input : 1
break
'''


import sys
input = sys.stdin.readline

def find_set(x):
    if arrival_info[x] != x:
        arrival_info[x] = find_set(arrival_info[x])
    return arrival_info[x]

def union(x, y):
    arrival_info[y] = x

G = int(input())
P = int(input())
arrival_info = [0] + [i for i in range(1, G + 1)]

max_docking = 0
# 비행기가 도착한다
for _ in range(P):
    gate = find_set(int(input()))
    if not gate:
        break
    union(find_set(arrival_info[gate - 1]), gate)
    max_docking += 1

print(max_docking)