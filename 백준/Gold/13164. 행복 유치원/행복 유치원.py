'''
n명의 원생들을 키 순서대로 세운다 -> 정렬
k개의 조로 나누고자 한다 : 일단 인접한 애들의 값을 구해줘야 댐
구한 다음, 인접한 값 위치를 오름차순으로 정렬한다.
그리고, k개만큼만 더해주고 나머지는 날려
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

adj_values = []
for adj_idx in range(1, n):
    adj_values.append(arr[adj_idx] - arr[adj_idx - 1])

adj_values.sort()
print(sum(adj_values[:n - k]))